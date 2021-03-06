# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Warp
def test_Warp_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    deoblique=dict(argstr='-deoblique',
    ),
    out_file=dict(name_source='in_file',
    name_template='%s_warp',
    argstr='-prefix %s',
    ),
    matparent=dict(argstr='-matparent %s',
    ),
    args=dict(argstr='%s',
    ),
    interp=dict(argstr='-%s',
    ),
    outputtype=dict(),
    zpad=dict(argstr='-zpad %d',
    ),
    mni2tta=dict(argstr='-mni2tta',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(position=-1,
    mandatory=True,
    argstr='%s',
    ),
    gridset=dict(argstr='-gridset %s',
    ),
    tta2mni=dict(argstr='-tta2mni',
    ),
    )
    inputs = Warp.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Warp_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Warp.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
