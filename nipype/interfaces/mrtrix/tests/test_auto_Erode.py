# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix.preprocess import Erode
def test_Erode_inputs():
    input_map = dict(out_filename=dict(position=-1,
    genfile=True,
    argstr='%s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    dilate=dict(position=1,
    argstr='-dilate',
    ),
    args=dict(argstr='%s',
    ),
    quiet=dict(position=1,
    argstr='-quiet',
    ),
    number_of_passes=dict(argstr='-npass %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(position=-2,
    mandatory=True,
    argstr='%s',
    ),
    debug=dict(position=1,
    argstr='-debug',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = Erode.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Erode_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Erode.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
