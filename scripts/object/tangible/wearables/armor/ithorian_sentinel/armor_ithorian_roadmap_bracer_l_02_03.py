import sys

def setup(core, object):
	object.setStfFilename('static_item_n')
	object.setStfName('armor_ithorian_roadmap_bracer_l_02_03')
	object.setDetailFilename('static_item_d')
	object.setDetailName('armor_ithorian_roadmap_bracer_l_02_03')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 3)
	object.setStringAttribute('class_required', 'Bounty Hunter')
	object.setStringAttribute('armor_category', 'Assault')
	object.setIntAttribute('cat_armor_standard_protection.kinetic', 2640)
	object.setIntAttribute('cat_armor_standard_protection.energy', 640)
	object.setIntAttribute('cat_armor_special_protection.special_protection_type_heat', 1640)
	object.setIntAttribute('cat_armor_special_protection.special_protection_type_cold', 1640)
	object.setIntAttribute('cat_armor_special_protection.special_protection_type_acid', 1640)
	object.setIntAttribute('cat_armor_special_protection.special_protection_type_electricity', 1640)
	return	
