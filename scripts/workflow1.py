from dessia_common.workflow.core import Workflow, Pipe
from dessia_common.workflow.blocks import InstantiateModel, ModelMethod, MultiPlot, MethodType

import hello_dessia as hd

block_generator = InstantiateModel(hd.Generator, name='Generator')
method_type = MethodType(class_=hd.Generator, name='generate')
methode_generate = ModelMethod(method_type=method_type, name='generate')
list_attribute = ['rivet_diameter', 'rivet_length', 'head_diameter',
                  'head_length', 'price', 'mass']
display = MultiPlot(list_attribute, 1, name='Display')

block_workflow = [block_generator, methode_generate, display]

pipe_worflow = [
    Pipe(block_generator.outputs[0], methode_generate.inputs[0]),
    Pipe(methode_generate.outputs[0], display.inputs[0])
]

workflow = Workflow(block_workflow, pipe_worflow,
                       methode_generate.outputs[0],
                       name='Hello Dessia')
workflow.plot()

rivets_definition = [[0.01, 0.05, 0.012, 0.005],
                     [0.012, 0.05, 0.013, 0.0055],
                     [0.0125, 0.05, 0.014, 0.0057],
                     [0.013, 0.05, 0.016, 0.006],
                     [0.014, 0.06, 0.018, 0.007],
                     [0.0145, 0.07, 0.0185, 0.0071],
                     [0.015, 0.075, 0.0186, 0.0073]]

input_values = {workflow.index(block_generator.inputs[0]): rivets_definition}
workflow_run = workflow.run(input_values)

# c = Client(api_url='https://api.platform-dev.dessia.tech')
# r = c.create_object_from_python_object(workflow_run)
