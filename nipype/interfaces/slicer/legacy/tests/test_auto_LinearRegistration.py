# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.legacy.registration import LinearRegistration
def test_LinearRegistration_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    initialtransform=dict(argstr='--initialtransform %s',
    ),
    histogrambins=dict(argstr='--histogrambins %d',
    ),
    translationscale=dict(argstr='--translationscale %f',
    ),
    movingsmoothingfactor=dict(argstr='--movingsmoothingfactor %d',
    ),
    args=dict(argstr='%s',
    ),
    outputtransform=dict(hash_files=False,
    argstr='--outputtransform %s',
    ),
    spatialsamples=dict(argstr='--spatialsamples %d',
    ),
    resampledmovingfilename=dict(hash_files=False,
    argstr='--resampledmovingfilename %s',
    ),
    MovingImageFileName=dict(position=-1,
    argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    learningrate=dict(argstr='--learningrate %s',
    sep=',',
    ),
    iterations=dict(argstr='--iterations %s',
    sep=',',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    FixedImageFileName=dict(position=-2,
    argstr='%s',
    ),
    fixedsmoothingfactor=dict(argstr='--fixedsmoothingfactor %d',
    ),
    )
    inputs = LinearRegistration.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_LinearRegistration_outputs():
    output_map = dict(resampledmovingfilename=dict(),
    outputtransform=dict(),
    )
    outputs = LinearRegistration.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
