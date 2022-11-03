import re

from flask import Flask, jsonify
from laun.laundry_fa import total_laundry

app = Flask(__name__)

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
#pendefinisian swager
app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'API Documentation for Data Processing and Modeling'),
        'version': LazyString(lambda: '1.0.0'),
        'description': LazyString(lambda: 'Dokumentasi API untuk Data Processing dan Modeling')
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json'
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,config=swagger_config)
#################################################

@swag_from("docs/laundry.yml", methods=['POST'])
@app.route('/laundry', methods=['POST'])
def laundry():
    na = request.json['nama']
    la = request.json['laundry']
    dc = request.json['dry_clean']
    m = request.json['member']

    nama_lower = na.lower()
    m_lower = m.lower()

    tot = total_laundry (nama_lower, int (la), int(dc), m_lower)

    print (tot)
    return (jsonify(tot))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2045)
