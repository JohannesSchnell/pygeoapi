

import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError
import xarray as xr
import tempfile

LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.2.0',
    'id': 'bbox',
    'title': {
        'en': 'bbox'
    },
    'description': {
        'en': 'crops nc file by bbox'
        
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['example', 'bbox'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'bbox': {
            'title': 'bbox',
            'description': 'max_lat,min_lat,max_lon,min_lon',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 0,
            'maxOccurs': 1,
            'metadata': None,  # TODO how to use?
            'keywords': ['bbox', 'lat,lon']
        }
    },
    'outputs': {
        'echo': {
            'title': 'cropped',
            'description': 'cropped by bbox',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/x-netcdf'
            }
        }
    },
    'example': {
        'inputs': {
            'bbox': '34.88,-26.37,72.86,31.99'
        }
    }
}


class BboxProcessor(BaseProcessor):
    """Hello World Processor example"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.bbox.BboxProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        mimetype = 'application/netcdf'
        
        bbox=data.get('bbox')
        if bbox is None:
            #raise ProcessorExecuteError('Cannot process without a name')
            bbox = '34.88,-26.37,72.86,31.99'

        coords = [float(i) for i in bbox.split(',')]

        lat_max=coords[0]
        lat_min=coords[1]
        lon_max=coords[2]
        lon_min=coords[3]



        data = xr.open_dataset('/workspaces/pygeoapi/data/20230720_PWAT_EATM_0.nc')
        cropped = data.sel(latitude=slice(lat_max,lat_min), longitude=slice(lon_min, lon_max))


        print(cropped)
        with tempfile.TemporaryFile() as fp:
                LOGGER.debug('Returning data in native NetCDF format')
                fp.write(cropped.to_netcdf())
                fp.seek(0)
                nc=fp.read()
                

                return mimetype, nc

    def __repr__(self):
        return f'<BboxProcessor> {self.name}'
