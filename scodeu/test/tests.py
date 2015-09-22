import unittest
import scodeu

"""
# text search seems broken

class TextSearchTest(unittest.TestCase):

    def setUp(self):
        self.client = scodeu.Client()
        
    def test_client_can_connect_to_provider(self):
        response = self.client.text_search('Mutriku')
        self.assertEqual(response['status_code'], 200)

    def test_client_returns_xml(self):
        # APIak ez du erantzuten
        response = self.client.text_search('Mutriku')
        self.assertIn(b'<?xml', response['content'])
"""
class CodifiedSearchTest(unittest.TestCase):

    def setUp(self):
        self.client = scodeu.RegistrosPublicosAdministrativos()

    def test_client_returns_xml(self):
        response = self.client.codified_search(
            tipo='asociacion',
            lang='eu')
        self.assertIn('<?xml', response['raw_content'])

class BaseClientTest(unittest.TestCase):
    
    def setUp(self):
        self.opendata = scodeu.OpenData()
        self.rpa = scodeu.RegistrosPublicosAdministrativos()
        # &r01kPgCmd=next&r01kSrchSrcId=contenidos.inter'
        self.base_query = 'http://www.euskadi.eus/r01hSearchResultWar/r01hPresentationXML.jsp?r01kLang=es&r01kQry='
        
    def test_metadata_filters(self):
        self.assertEqual('', self.opendata._build_metadata_string())
        bad_metadata = ((),)
        self.assertEqual('', self.opendata._build_metadata_string(metadata_filters=bad_metadata))
        bad_metadata = (('metadataName', 'FilterOperator',),)
        self.assertEqual('', self.opendata._build_metadata_string(metadata_filters=bad_metadata))
        good_metadata = (('OpendataFormats', 'IN', 'XML'),)
        self.assertEqual('m:OpendataFormats.IN.XML', self.opendata._build_metadata_string(metadata_filters=good_metadata))
        self.assertEqual('cO:OpendataFormats.IN.XML', self.opendata._build_metadata_string(metadata_filters=good_metadata, metadata_operator='OR'))
        self.assertEqual('m:OpendataFormats.IN.XML', self.opendata._build_metadata_string(metadata_filters=good_metadata, metadata_operator='BADFILTER'))
        multiple_metadata = (('OpendataFormats', 'IN', 'XML'), ('OpendataLicense', 'EQ', 'GPL'))
        self.assertEqual('m:OpendataFormats.IN.XML,OpendataLicense.EQ.GPL', self.opendata._build_metadata_string(metadata_filters=multiple_metadata))
        
    def test_order_filters(self):
        self.assertEqual('', self.opendata._build_order_string())
        bad_order = ((),)
        self.assertEqual('', self.opendata._build_order_string(order_filters=bad_order))
        bad_order = (('metadataName', 'OrderOperator'),)
        self.assertEqual('', self.opendata._build_order_string(order_filters=bad_order))
        good_order = (('statisticDiffusionDate', 'DESC'),)
        self.assertEqual('o:statisticDiffusionDate.DESC', self.opendata._build_order_string(order_filters=good_order))        
        
    def test_build_correct_codified_search_url(self):
        self.maxDiff = None
        
        correct_codified_url = self.base_query + 'tC:euskadi;tF:registros_publicos_administrativos;tT:asociacion;m:documentLanguage.EQ.es,recTerritoryCode.EQ.1,recTownCode.EQ.1;o:documentCreateDate.DESC;pp:r01PageSize.100'
        metadata = (('documentLanguage', 'EQ', 'es'), ('recTerritoryCode', 'EQ', '1'), ('recTownCode', 'EQ', '1'))
        ordering = (('documentCreateDate', 'DESC'),)
        
        self.assertEqual(correct_codified_url, self.rpa._build_search_url(
            search_type='codified',
            lang='es',
            tipo='asociacion',
            metadata=metadata,
            order=ordering))
        
    def test_build_correct_fulltext_search_url(self):
        correct_fulltext_url = self.base_query + 'Mutriku Ondarroa&resultsSource=fullText;pp:r01PageSize.100'
        self.assertEqual(correct_fulltext_url, self.rpa._build_search_url(
            search_type='fulltext',
            lang='es',
            search_text='Mutriku Ondarroa'))
        
        correct_fulltext_AND_url = self.base_query + 'Mutriku+Ondarroa&resultsSource=fullText;pp:r01PageSize.100'
        self.assertEqual(correct_fulltext_AND_url, self.rpa._build_search_url(search_type='fulltext',lang='es',
                                                                               search_text='Mutriku Ondarroa',
                                                                               search_operator='+'))

    def test_response_includes_items_itemcount_totalitems_pagination_data(self):
        response = self.rpa.codified_search(
            tipo='asociacion',
            lang='eu')
        self.assertEqual(type(response.get('items')), type([]))
        self.assertIn('total', response.keys())
        self.assertIn('more', response.keys())

    def test_response(self):
        response = self.rpa.codified_search(
            tipo='asociacion',
            lang='eu')
        self.assertEqual(len(response.get('items')), 100)
        self.assertEqual(response.get('total'), 18069) # Risky test, based on search count at 2015/09/17
        self.assertEqual(response.get('more'), 2)

    def test_pagination(self):
        response = self.rpa.codified_search(
            tipo='asociacion',
            lang='eu',
            page=2)
        self.assertEqual(response.get('more'), 3)
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
