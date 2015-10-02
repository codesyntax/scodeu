from .client import Client

class AnunciosAdministrativos(Client):
    allowed_types = ('informacion_publica',)
    
    common_metadata = ('pubInfExpCode',
                       'pubInfExpTitle',
                       'pubInfType',
                       'pubInfBeginDate',
                       'pubInfEndDate')

    familia = 'anuncios_administrativos'

class AvisosTecnicos(Client):
    allowed_types = ('aviso_tecnico',)

    common_metadata = ('noticeTile',
                       'noticeDescription',
                       'noticeActivationDate',
                       'noticeExpirationDate',
                       'noticeIntenalScopeContents',
                       'noticeIntenalScopePortals',
                       'noticeExternalScope',
                       'noticeSystemInternet',
                       'noticeSystemsSite',
                       'noticeDetail',
                       'noticeIncidence',
                       'noticeSolved',
                       'noticeIncidenceDate',
                       'noticeIncidenceResolutionDate')

    familia = 'avisos_tecnicos'
        
class BOPV(Client):
    allowed_types = ('bopv_recurso_inconst',
                     'bopv_cuestion_inconst',
                     'bopv_recurso_amparo',
                     'bopv_conflicto_positivo',
                     'bopv_conflicto_negativo',
                     'bopv_ley',
                     'bopv_decreto_ley',
                     'bopv_decreto_legis',
                     'bopv_norma_foral',
                     'bopv_real_decreto',
                     'bopv_decreto',
                     'bopv_decreto_foral',
                     'bopv_orden',
                     'bopv_orden_foral',
                     'bopv_acuerdo',
                     'bopv_resolucion',
                     'bopv_circular',
                     'bopv_anuncio',
                     'bopv_edicto',
                     'bopv_anuncio_l',
                     'bopv_anuncio_a'
                     )

    common_metadata = ()

    familia = 'bopv'


class Catalogos(Client):
    allowed_types = ('catalogo_acreditacion',
                     'catalogo_beneficiario',
                     'catalogo_tramite',
                     )

    common_metadata = ()

    familia = 'catalogos'

class CompetenciaYTransferencias(Client):
    allowed_types = ('transderencia',
                     'competencia',
                     )

    common_metadata = ('statuteTitle',
                       'statuteObject',
                       'statuteState',
                       'statuteYear'
                       )
    familia = 'competencia_y_transferencias'

class DiccionarioEnciclopedia(Client):
    allowed_types = ('articulo',
                     'termino',
                     )

    common_metadata = ('enctermino',
                       'encdescripcion',
                       )

    familia = 'diccionario_enciclopedia'


class Directorios(Client):
    allowed_types = ('centro',
                     'contacto',
                     'biblioteca',
                     'poder_adjudicador',
                     'punto_informacion_juvenil'
                     )

    common_metadata = ('libName', # biblioteca metadata
                       'libType',
                       'libOrgType',
                       'libAccessType',
                       'libCategory',
                       'libTheme',
                       'libSBNE',
                       'libBilgunea',
                       'poder_adjudicador_titulo', # poder adjudicador metadata
                       'poder_adjudicador_descripcion',
                       'poder_adjudicador_logo',
                       'poder_adjudicador_url_web_oficial',
                       'poder_adjudicador_ambito',
                       'poder_adjudicador_fecha_publicacion_documento',
                       'locationCountry', # punto informacion juvenil metadata
                       'locationProvincia',
                       'locationTown',
                       'locationCP',
                       )

    familia = 'directorios'


class Documentacion(Client):
    allowed_types = ('plan_prgrama_proyecto',
                     'informe_estudio',
                     'memoria',
                     'inventario',
                     'manual'
                     )

    common_metadata = ('docType',
                       'docPublishDate',
                       'docNumber',
                       'subType', # plan programa proyecto metadata
                       'projectTitle',
                       'projectStartDate',
                       'projectEndDate',
                       'projectStatus',
                       'projectLastModifiedDate',
                       'planStatus',
                       'lawProjectStatus',
                       'actionStatus',
                       'planPhase')
        
    familia = 'documentacion'


class DocumentacionJuridica(Client):
    allowed_types = ('dictamen',
                    'doctrina',
                    'resolucion_oarc',
                    )

    common_metadata = ('legalDocTitle',
                       'legalDocLeading',
                       'legalDocAuthor',
                       'legalDocPublishDate')
        
    familia = 'documentacion_juridica'
    

class Enlaces(Client):
    allowed_types = ('enlaces',
                     'sercicio_online',
                     )

    common_metadata = ()
    familia = 'enlaces'
    

class Eventos(Client):
    allowed_types = ('evento',)

    common_metadata = ('eventType',
                       'eventStartDate',
                       'eventEndDate',
                       'eventCountry',
                       'eventTerritory',
                       'eventTerritoryName',
                       'eventTown',
                       'eventToenName',
                       'eventLocation',
                       'eventLocationName',
                       'eventWhere',
                       'eventSponsor',
                       'eventSearchDate1',
                       'eventSearchDate2',
                       'importance',
                       'profile',
                       'parentcorec',
                       'marks',
                       'general',
                       'templateType',
                       'touristOffice',
                       )
    familia = 'eventos'
    

class InformacionGeneral(Client):
    allowed_types = ('informacion',
                     'anuncio_tablon_contratacion',
                     'faq',
                     'recurso_tecnico',
                     )

    common_metadata = ('dataWhere', # informacion metadata
                       'modifiedDate',
                       'materiafaq', # faq metadata
                       'tematicafaq',
                       'fechafaq',
                       'normativafaq',
                       'anuncio_tablon_contratacion_titulo', # anuncio tablon contratacion metadata
                       'anuncio_tablon_contratacion_descripcion',
                       'anincio_tablon_contratacion_tipo',
                       )
    familia = 'informacion_general'

class Legislacion(Client):
    allowed_types = ('normativa',
                     'convenio',
                     )

    common_metadata = ('conventionTitle', # convenio metadata
                       'conventionObject',
                       'conventionDate'
                       )

    familia = 'legislacion'

    
class Localizacion(Client):
    allowed_types = ('promocion',
                     'estacion_meteo',
                     'lugar_culto')

    common_metadata = ('promTitle', # promocion metadata
                       'promAreaTxt',
                       'promCity',
                       'promHousingType',
                       'promOwnerType',
                       'promDrawDate',
                       'promState',
                       'promExpedient',
                       'promTotalHomes',
                       'promLatitude',
                       'promLongitude',
                       )

    familia = 'localizacion'
    
class Meteorologia(Client):
    allowed_types = ('prevision_tiempo',
                     'prevision_maritima',
                     'tendencias',
                     'mapas',
                     'avisos')

    common_metadata = ('meteoDateStart', # prevision_tiempo
                       'meteoDateText',
                       'meteoMap',
                       'meteoForecastText',
                       'meteoForecastIcon',
                       'meteoArabaMaxTemp',
                       'meteoArabaMinTemp',
                       'meteoArabaTemp',
                       'meteoArabaIcon',
                       'meteoBizkaiaMaxTemp',
                       'meteoBizkaiaMinTemp',
                       'meteoBizkaiaTemp',
                       'meteoBizkaiaIcon',
                       'meteoGipuzkoaMaxTemp',
                       'meteoGipuzkoaMinTemp',
                       'meteoGipuzkoaTemp',
                       'meteoGipuzkoaIcon',
                       'meteoSeaMap', # prevision_maritima metadata
                       'meteoSeaForecast',
                       'meteoIconSeaWind',
                       'meteoIconWave',
                       'meteoSunrise',
                       'meteoSunset',
                       'meteoMoonStart',
                       'meteoMoonEnd',
                       'meteoHighTideTime1',
                       'meteoHighTideMeters1',
                       'meteoHighTideTime2',
                       'meteoHighTideMeters2',
                       'meteoLowTideTime1',
                       'meteoLowTideMeters1',
                       'meteoLowTideTime2',
                       'meteoLowTideMeters2',
                       'meteoSeaTemp',
                       'meteoVisibility',
                       'meteoDateEnd', # tendencias metadata
                       'meteoIconDay1',
                       'meteoIconDay2',
                       'meteoIconDay3',
                       'meteoIconDay4',
                       'meteoIconDay5',
                       'meteoIconDay6',
                       'meteoIconTrend1',
                       'meteoIconTrend2',
                       'meteoIconTrend3',
                       'meteoIconTrend4',
                       'meteoIconTrend5',
                       'meteoIconTrend6',
                       'meteoIconWind1',
                       'meteoIconWind2',
                       'meteoIconWind3',
                       'meteoIconWind4',
                       'meteoIconWind5',
                       'meteoIconWind6',
                       'meteoMap', # mapas metadata
                       'MeteoAdviceLevel', #avisos metadata
                       'meteoAdviceText'
                        )
    familia = 'metereologia'


class Normativa(Client):
    familia = 'normativa'
    allowed_types = ('constitucion',
                     'ley_organica',
                     'ley',
                     'decreto_ley',
                     'decreto_legislativo',
                     'real_decreto',
                     'real_decreto_ley',
                     'real_decreto_legislativo',
                     'decreto',
                     'orden',
                     'norma',
                     'resolucion',
                     'circular',
                     'orientacion',
                     'decision',
                     'directiva',
                     'acuerdo',
                     'convenio_normativa',
                     'instruccion',
                     'reglamento',
                     'conflicto_positivo',
                     'conflicto_negativo',
                     'recurso_amparo',
                     'recurso_inconst',
                     'cuestion_inconst',
                     'otra_normativa',
                     )

    common_metadata = ('normTitle',
                       'normField',
                       'normTypeOB',
                       'normNumberOB',
                       'normOrderNumberOB',
                       'normDispositionNumber',
                       'normDispositionDate',
                       'normPublicationDate',
                       'normBodyEText',
                       'normStatus',
                       'normConsolidatedTextFlag',
                       )
                           

class OpenData(Client):
    # http://opendata.euskadi.eus/contenidos-generales/-/contenidos/informacion/inventario_familias_tipos/es_def/imgpreview.shtml?index=16
    
    allowed_types = ('estadistica',
                     'ds_meteorologicos',
                     'ds_geograficos',
                     'ds_recursos_turisticos',
                     'ds_recursos_linguisticos',
                     'ds_ayudas_subvenciones',
                     'ds_autorizaciones',
                     'ds_carnes',
                     'ds_registros',
                     'ds_inspecciones',
                     'ds_multas_sanciones',
                     'ds_arbitrajes_denuncias_reclamaciones',
                     'ds_contrataciones',
                     'ds_premios_concursos',
                     'ds_procedimientos_otros',
                     'ds_anuncios_contratacion',
                     'ds_general',
                     'ds_informes_estudios',
                     'ds_localizaciones',
                     'ds_noticias',
                     'ds_eventos',
                     'ds_rrhh',
                     'ds_juridicos',
                     'ds_organizacion',)
        
    common_metadata = ('statisticOfficiality',
                       'statisticRegularity',
                       'statisticDiffusionDate',
                       'OpendataEstadistic',# (sic)
                       'OpendataTextHTML',
                       'OpendataURLHTML',
                       'OpendataImageEustat',
                       'OpendataDatasets',
                       'OpendataLabels',
                       'OpendataSource',
                       'OpendataReleaseDate',
                       'OpendataOrder',
                       'OpendataFormats',
                       'OpendataLicense',)
    familia = 'opendata'


class Organizacion(Client):
    familia = 'organizacion'

    allowed_types = ('institucion',
                     'organo',)

    common_metadata = ()


class PrensaYComunicacion(Client):

    familia = 'prensa_y_comunicacion'

    allowed_types = ('noticia',
                     'nota_prensa',
                     'publicidad',
                     'acuerdo_gobierno',
                     'acuerdo_gobierno_sesion',
                     )

    common_metadata = ('commDate',
                       'topic',
                       'importance', # noticia metadata
                       'general',
                       'touristOffice',
                       'subtema1', # publicidad and acuerdo gobierno sesion metadata
                       )

class ProcedimientosAdministrativos(Client):
    familia = 'procedimientos_administrativos'

    allowed_types = ('ayuda_subvencion',
                     'planes_ayudas',
                     'autorizacion',
                     'carnet',
                     'registro',
                     'inspeccion',
                     'multa_sancion',
                     'arbitraje_denuncia_reclamacion',
                     'contratacion',
                     'premio_concurso',
                     'procedimiento_otro',
                     'anuncio_contratacion',
                     'censo',
                     'procedimiento_iniciado_administracion',
                     )

    common_metadata = ('procedureDenominacion',
                       'procedureStartDate',
                       'procedureEndDate',
                       'procedureStatus',
                       'procedureSolved',
                       'procedureHistorical',
                       'procedureOnLine',
                       'procedureOnLinePayment',
                       'procedureOnLineNotify',
                       'procedureOnLineQuery',
                       'procedureResolution',
                       'procedureValidity',
                       'prdAdvType', # contratacion metadata
                       'prcStatus',
                       'contratacion_titulo_contrato', # anuncio_contratacion metadata
                       'contratacion_objecto_contrato',
                       'contratacion_tipo_anuncio',
                       'contratacion_fecha_de_publicacion_documento',
                       'contratacion_expediente',
                       'contratacion_estado_tramitacion',
                       'contratacion_adjudicacion',
                       'contratacion_subsanacion',
                       'contratacion_apertura_plicas',
                       'contratacion_acuerdos_mesa_contratacion',
                       'contratacion_ambito_geografico',
                       'contratacion_poder_adjudicador_url',
                       'contratacion_poder_adjudicador_titulo',
                       'contratacion_entidad_impulsora',
                       'contratacion_organo_contratacion',
                       'contratacion_tipo_contrato',
                       'contratacion_materia_contrato',
                       'contratacion_fecha_limite_presentacion'
                       )
                     

class Publicacion(Client):
    familia = 'publicacion'

    allowed_types = ('libro',
                     'boletin_revista',
                     )

    common_metadata = ('subtema1',)


class RecursosHumanos(Client):
    familia = 'recursos_humanos'

    allowed_types = ('rrhh',
                     'empleo_publico',
                     'empleo_publico_ope',
                     )

    common_metadata = ('rrhhStartDate',
                       'rrhhEndDate',
                       'rrhhSponsor',
                       'rrhhTerritory',
                       'rrhhTown',
                       'rrhhVacancies',
                       'rrhhRules',
                       'rrhhTexts',
                       'rrhhLists',
                       'rrhhWhere', # rrhh metadata
                       'rrhhSummary',
                       'rrhhType', # empleo publico metadata
                       )
        
class RegistrosPublicosAdministrativos(Client):
    # http://opendata.euskadi.eus/contenidos-generales/-/contenidos/informacion/inventario_familias_tipos/es_def/imgpreview.shtml?index=22

    allowed_types = ('fundacion',
                     'asociacion')

    common_metadata = ('recNumRec'
                       'recName',
                       'recConstitutionDate',
                       'recTerritoryCode',
                       'recTerritoryName',
                       'recTownCode',
                       'recTownName',
                       'recPostalCode',
                       'recAddress',
                       'recGoal')
        
    familia = 'registros_publicos_administrativos'

class Sanidad(Client):
    familia = 'sanidad'

    allowed_types = ('sanidad_causa_mortalidad',)

    common_metadata = ()


class SanidadUbicaciones(Client):
    familia = 'sanidad_ubicaciones'

    allowed_types = ('sanidad_hospital',
                     'sanidad_farmacia',
                     'sanidad_centro',
                     'sanidad_comarca',
                     'sanidad_inspeccion',
                     'sanidad_botiquin',
                     )

    common_metadata = ('sanidadCode',
                       'sanidadName',
                       'sanidadAlias',
                       'sanidadCenterType',
                       'sanidadStreet',
                       'sanidadPostalCode',
                       'sanidadTown',
                       'sanidadProvince',
                       'sanidadRegion',
                       'sanidadTimeTable',
                       'sanidadSpecialTimeTable'
                       )


class Servicios(Client):
    familia = 'familia'

    allowed_types = ('formulario',
                     'canal_telematico',
                     'catalogo_tramite',
                     'convocatoria',
                     'guia_rapida_zuzenean',
                     )
        
    common_metadata = ('formType', # formulario metadata
                       'serviceName',
                       'serviceDescription',
                       'serviceUrl',
                       'formLastModifiedDate',
                       'formInitDate',
                       'formEndDate'
                       'aplicType', # canal_tematico metadata
                       'aplicAutentificationType',
                       'callWhere', # convocatoria metadata
                       'callStartDate',
                       'callEndDate',
                       'callSponsor',
                       'callSummary'
                       )

class Turismo(Client):
    familia = 'turismo'

    allowed_types = ('a_alojamiento',
                     'b_restauracion',
                     'c_transporte_y_movilidad',
                     'd_destinos_turisticos',
                     'e_oficinas_turisticas',
                     'g_naturaleza',
                     'h_cultlura_y_patimonio',
                     'i_deportes',
                     'j_gastronomia',
                     'k_ocio',
                     'l_compras',
                     'n_negocios'
                     )

    common_metadata = ('templateType',
                       'historicTerritory',
                       'historicTerritoryCode',
                       'municipality',
                       'municipalityCode',
                       'locality',
                       'localityCode',
                       'qualityQ',
                       'qualityIconURL',
                       'qualityIconDescription',
                       'accesibility',
                       'accesibilityIconURL',
                       'accesibilityIconDescription',
                       'phoneNumber',
                       'address',
                       'order',
                       'marks',
                       'profile',
                       'physical',
                       'visual',
                       'auditive',
                       'intellectual',
                       'organic',
                       'qualityAssurance',
                       'email',
                       'web',
                       'importance',
                       'general',
                       'months',
                       'touristOffice',
                       'room',
                       'lodgingType', # a_alojamiento metadata
                       'category',
                       'priceHigh',
                       'priceLow',
                       'restorationType', # b_restauracion metadata
                       'recomended',
                       'recomendedURLIcon',
                       'visit',
                       'menu',
                       'restaurant',
                       'bodega',
                       'transportType', # c_transporte_y_movilidad metadata
                       'car',
                       'howtoarrive',
                       'howtomove',
                       'type', # d_destinos_turisticos metadata
                       'duration',
                       'transportType',
                       'routeInitPoint',
                       'routeEndPoint',
                       'experienceDuration',
                       'water',
                       'landscape',
                       'cuisine',
                       'culture',
                       'couple',
                       'children',
                       'friends',
                       'searchable',
                       'routeType',
                       'languages',
                       'visit', # e_oficinas_turisticas metadata
                       'natureType', # g_naturaleza metadata
                       'cultureType', # h_cultura_y_patrimonio metadata
                       'subtype',
                       'sportType', # i_deportes metadata
                       'gastronomyType', # j_gastronomia
                       'funType', # k_ocio metadata
                       'category',
                       'buyType', # l_compras metadata
                       'sectorType', # n_negocios metadata
                       )
