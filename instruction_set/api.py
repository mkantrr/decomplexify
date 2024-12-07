from flask import Flask, jsonify, request
import os
import sys
from behave.__main__ import Configuration, run_behave

from behave_runner import AgentBasedModelingRunner
import globals
from executive_main import setup_files

api = Flask(__name__)

# Function to create text files from data
def create_text_files(data):
    # Create a directory to store the files
    if not os.path.exists('features'):
        os.makedirs('features')

    # Iterate through each key-value pair and write to a text file
    for key, value in data.items():
        with open(os.path.join('features', f"{key}.feature"), 'w') as f:
            f.write(value)
            
def run_behave():
    orig_stdout = sys.stdout
    f = open('behave.out', 'w')
    sys.stdout = f
    
    globals.init()
    
    setup_files() 
    config = Configuration(verbose=True)
    retval = run_behave(config, runner_class=AgentBasedModelingRunner)
    if retval != 0:
         raise SystemError("Behave could not run properly. Check your syntax!")
    #os.remove('features/steps/generated_functions.py')
    #os.remove('features/steps/agent_classes.py')
    
    sys.stdout = orig_stdout
    f.close()

# Endpoint to handle the creation of text files
@api.route('/create', methods=['POST'])
def create_files():
    # Get JSON data from the request
    data = request.json

    # Ensure there are exactly 5 keys
    if len(data) != 4:
        return jsonify({'error': 'Request does not contain the correct amount of model definitions!'}), 400
    
    try:
        # Call the function to create text files
        create_text_files(data)
        run_behave() 
        return jsonify({'message': 'Model definition files created successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Endpoint to handle the creation of text files
@api.route('/model-data', methods=['GET'])
def fetch_model_dataframe():
    try:
        data = globals.MODEL.datacollector.get_model_vars_dataframe().to_json(orient='split')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to handle the creation of text files
@api.route('/agent-data', methods=['GET'])
def fetch_agent_dataframe():
    try:
        data = globals.MODEL.datacollector.get_agent_vars_dataframe().to_json(orient='split')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@api.route('/step-once', methods=['GET'])
def step_once():
    try:
        globals.MODEL.step()
        return jsonify({'key': type(globals.MODEL.grid).__name__, 
                        'width': globals.MODEL.grid.width,
                        'height': globals.MODEL.grid.height,
                        'data': globals.MODEL.get_single_grid_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    api.run(debug=True)