import json
from flask import Flask, request,Blueprint,jsonify
from pkg.utils.exp import process_images


exp_api = Blueprint('exp_api', __name__)


@exp_api.route('/exp-api', methods=['POST'])
def detect_dates():
    try:
        # Get file path from request
        image_path = request.json.get('img_path')

        # Process the single image to detect dates
        date_info = process_images([image_path])

        # Convert the dictionary to JSON format without trailing commas
        # date_data = json.dumps(date_info, indent=4, separators=(',', ':'))

        return jsonify(date_info)

    except Exception as e:
        return str(e), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001, debug=True)
