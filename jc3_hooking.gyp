{
	'targets': [
	{
		'target_name': 'jc3_hooking',
		'type': 'static_library',
		'all_dependent_settings': {
            'include_dirs': ['.'],
         },
		'dependencies': [
			'libudis86',
		],
		'sources': [
			'jc3_hooking/hooking.cpp',
			'jc3_hooking/hooking.h',
			'jc3_hooking/udis86.h',
			'jc3_hooking/jitasm.h',
		],
	},
	{
		'target_name': 'libudis86',
		'type': 'static_library',
		'sources': [
			'jc3_hooking/libudis86/decode.h',
			'jc3_hooking/libudis86/extern.h',
			'jc3_hooking/libudis86/itab.h',
			'jc3_hooking/libudis86/syn.h',
			'jc3_hooking/libudis86/types.h',
			'jc3_hooking/libudis86/udint.h',

			'jc3_hooking/libudis86/decode.c',
			'jc3_hooking/libudis86/itab.c',
			'jc3_hooking/libudis86/syn.c',
			'jc3_hooking/libudis86/syn-att.c',
			'jc3_hooking/libudis86/syn-intel.c',
			'jc3_hooking/libudis86/udis86.c',
		],
	},
	]
}