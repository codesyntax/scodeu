import io
import requests
import xml.etree.ElementTree as etree

"""
m:documentLanguage.EQ.es,recTerritoryCode.EQ.%(probintzia_id)s,recTownCode.EQ.%(herria_id)s;o:documentCreateDate.DESC;pp:r01PageSize.100&r01kPgCmd=next&r01kSrchSrcId=contenidos.inter
"""
class Client(object):
    metadata = ('itemNumber',
                'score',
                'contentOid',
                'contentName',
                'contentDescription',
                'contentLocation',
                'contentTypology',
                'contentEditURL',
                'contentPreviewURL',
                'contentViewUrl',
                'structureCatalogs',
                'geoCatalogs',
                'documentOid',
                'documentInternalName',
                'documentCreateDate',
                'documentLanguage',
                'documentName',
                'documentDescription',
                'documentStatus',
                'documentMetaData',
                'documentEditURL',
                'documentPreviewURL',
                'dataFileOid',
                'dataFileName',
                'dataFileResume',
                'dataFileEditURL',
                'dataFilePreviewURL',
                'dataFileViewURL')
        
    allowed_types = ()
    common_metadata = ()
    endpoint = 'http://www.euskadi.eus/r01hSearchResultWar/r01hPresentationXML.jsp?r01kLang={0}&r01kQry={1}'
    
    def _build_metadata_string(self, metadata_filters=(), metadata_operator='AND'):
        """
        metadata_filters => (('metadata','filter_type','filter_value'),)
        metadata_operator: m for AND queries
                           cO dor OR queries
        filter_types => text -> EQ,LIKE
                        number -> EQ,NEQ,LTE,GTE
        """
        base = ''
        last = len(metadata_filters) - 1
        operators = {'OR': 'cO:',
                     'AND': 'm:'}
        valid_metadata = self.metadata + self.common_metadata
        for i,query_filter in enumerate(metadata_filters):
            if len(query_filter) == 3:
                if query_filter[0] in valid_metadata:
                    base += '.'.join(query_filter)
                    if i != last:
                        base += ','
        if base != '':
            base = operators.get(metadata_operator, 'm:') + base
        return base
    
    def _build_order_string(self, order_filters=()):
        """
        order => (('metadata','ordenation_type:ASC|DESC'),)
    
        """
        base =''
        last = len(order_filters) - 1
        valid_metadata = self.metadata + self.common_metadata
        for i,elem in enumerate(order_filters):
            if len(elem) == 2:
                if elem[0] in valid_metadata:
                    base += '.'.join(elem)
                    if i != last:
                        base += ','
        if base != '':
            base = 'o:' + base
        return base

    def _build_search_url(self, search_type, **kwargs):
        search_url = None
        search_string = ''
        lang = kwargs.get('lang', 'eu')
        page = kwargs.get('page', 1)
        
        if search_type == 'fulltext':
            search_template = '{0}&resultsSource=fullText'
            search_text = kwargs.get('search_text')
            operator = kwargs.get('search_operator', ' ')
            if operator == '+':
                search_text = operator.join(search_text.split())
            search_string = search_template.format(search_text)
        else:
            tipo = kwargs.get('tipo', '')
            if tipo in self.allowed_types:
                metadata_string = ''
                order_string = ''
                search_string = 'tC:euskadi;tF:{0};tT:{1}'.format(self.familia, tipo)
                metadata_string = self._build_metadata_string(kwargs.get('metadata', ()))
                if metadata_string is not '':
                    search_string = search_string + ';' + metadata_string
                order_string = self._build_order_string(kwargs.get('order', ()))    
                if order_string is not '':
                    search_string = search_string + ';' + order_string
        if search_string is not '':
            results_per_page = kwargs.get('results_per_page', 100)
            search_string += ';pp:r01PageSize.{0}'.format(results_per_page)
            search_url = self.endpoint.format(lang,search_string)
            if page != 1:
                search_url += '&r01kPgCmd=next&r01kSrchSrcId=contenidos.inter&r01kTgtPg={0}'.format(page)
            return search_url
        
    def _get_documents_oids(self, xml_item):
        """
        Recuperar el valor datafileOid es un poco complicado,ya que va en el nombre del tag
        Esta pendiente meter la url del documento directamente en la zona
        contentRispDocumentsInfo. De momento no esta disponible
        """
        document_oids_list = []
        for child in xml_item.getiterator():
            if child.tag.startswith('datafileOid'):
                document_oids_list.append(child.tag.split('.')[1])
        return document_oids_list
    
    def _create_item_from_xml(self, xml_item):
        #alid_metadata = self.metadata + self.common_metadata
                
        new_item = {}
        
        for child in xml_item.getiterator():
            if child.tag == 'documentDataFilesGeneratedFilesDocumentRelativePaths':
                new_item['datafileOids'] = self._get_documents_oids(child)
            new_item[child.tag] = child.text
                     
        return new_item

    def _parse_response(self, response):
        tree = etree.parse(io.StringIO(response.text))
        root = tree.getroot()
        items = root.findall('.//item')
        
        item_list = []
        for item in items:
            item_list.append(self._create_item_from_xml(item))
        search_source = root.find('.//navBar')
        total_items = int(search_source.get('totalNumberOfResults'))
        total_pages = int(search_source.get('totalNumberOfPages'))
        current_page = int(search_source.get('currentPage'))
        return item_list, total_items, total_pages, current_page
    
    def _search_do(self, url):
        response = {'status_code': None,
                    'items': [],
                    'total': 0,
                    'next': ''}
        if url:    
            euskadinet_response = requests.get(url)
            items, total_items, total_pages, current_page = self._parse_response(euskadinet_response)
            response['status_code'] = euskadinet_response.status_code
            response['raw_content'] = euskadinet_response.text
            response['items'] = items 
            response['total'] = total_items
            if current_page < total_pages:
               response['more'] = int(current_page ) + 1
        return response
    
    def text_search(self, text, lang='eu', operator=' '):
        url = self._build_search_url(search_type='fulltext',
                                     lang=lang,
                                     search_text=text,
                                     search_operator=operator)
        return self._search_do(url)
    
        
    def codified_search(self, tipo, **kwargs):
        """
        Familia eta tipo informazioa hemen:
        http://opendata.euskadi.eus/contenidos-generales/-/familias-y-tipos-de-contenido-de-euskadi-net/
        """
        build_url = self._build_search_url(search_type='codified', tipo=tipo, **kwargs)
        return self._search_do(build_url)

    
