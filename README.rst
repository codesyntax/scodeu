Search Client for Open Data EUskadi
===================================

This library provides a Python interface for the Euskadi.eus search engine.


Installation
------------

The preferred way of installing is using pip::
  
    pip install scodeu

Usage
-----

This is a minimal search operation in OpenData family for metheorological documents in basque::

  >>> import scodeu
  >>> client = scodeu.OpenData()
  >>> data = client.codified_search(tipo='ds_meteorologicos',
                                    lang='eu')
  >>> items = data.get('items')
  
Families
--------

Documents in euskadi.eus are organized in families. Every family defines its allowed content types and metadata. Metadata is used to filter results inside a content type.

Every families in euskadi.eus are available using scodeu. Best place to see available families, common metadata and allowed types  is in the families.py file.


References
----------

Theese are the base documents used to create scodeu

Information about `available families, metadata and allowed types`_.

.. _available families, metadata and allowed types: http://opendata.euskadi.eus/contenidos-generales/-/familias-y-tipos-de-contenido-de-euskadi-net/

Search engine `users manual`_ (pdf).

.. _users manual: http://opendata.euskadi.eus/contenidos/informacion/como_reutilizar_datos/es_def/adjuntos/opendataeuskadi_tech_manualbuscador.pdf


Pseudo-REST API `information`_.

.. _information: http://opendata.euskadi.eus/w79-utilizar/es/contenidos/informacion/api_buscador_euskadinet/es_java/como_utilizar.html

LICENSE
-------

This software is licensed as is under GPL v3 license.

CONTRIBUTING
------------

Please send your PR to the projects Github_ page.

.. _github: https://github.com/codesyntax/scodeu
