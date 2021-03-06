# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.model import Binarize
def test_Binarize_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    binary_file=dict(argstr='--o %s',
    genfile=True,
    ),
    count_file=dict(argstr='--count %s',
    ),
    frame_no=dict(argstr='--frame %s',
    ),
    bin_val_not=dict(argstr='--binvalnot %d',
    ),
    zero_edges=dict(argstr='--zero-edges',
    ),
    bin_val=dict(argstr='--binval %d',
    ),
    rmin=dict(argstr='--rmin %f',
    ),
    min=dict(xor=['wm_ven_csf'],
    argstr='--min %f',
    ),
    invert=dict(argstr='--inv',
    ),
    erode2d=dict(argstr='--erode2d %d',
    ),
    abs=dict(argstr='--abs',
    ),
    in_file=dict(copyfile=False,
    mandatory=True,
    argstr='--i %s',
    ),
    match=dict(argstr='--match %d...',
    ),
    zero_slice_edge=dict(argstr='--zero-slice-edges',
    ),
    out_type=dict(argstr='',
    ),
    erode=dict(argstr='--erode  %d',
    ),
    max=dict(xor=['wm_ven_csf'],
    argstr='--max %f',
    ),
    wm=dict(argstr='--wm',
    ),
    args=dict(argstr='%s',
    ),
    rmax=dict(argstr='--rmax %f',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    wm_ven_csf=dict(xor=['min', 'max'],
    argstr='--wm+vcsf',
    ),
    subjects_dir=dict(),
    ventricles=dict(argstr='--ventricles',
    ),
    bin_col_num=dict(argstr='--bincol',
    ),
    dilate=dict(argstr='--dilate %d',
    ),
    merge_file=dict(argstr='--merge %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    mask_thresh=dict(argstr='--mask-thresh %f',
    ),
    mask_file=dict(argstr='--mask maskvol',
    ),
    )
    inputs = Binarize.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Binarize_outputs():
    output_map = dict(count_file=dict(),
    binary_file=dict(),
    )
    outputs = Binarize.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
