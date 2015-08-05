from . properties import *
from . operator import *

def displayViewportInfoPanel(self, context):
    layout = self.layout    
    show_text = context.window_manager.show_text
    
    row = layout.row(align=True)
    row.prop(show_text, "vp_info_display_panel", text ="")
    if show_text.vp_info_enabled:
        row.operator('view3d.adh_display_text', text="Viewport info", icon='RESTRICT_VIEW_OFF' )                                
    else:
        row.operator('view3d.adh_display_text', text="Viewport info", icon='RESTRICT_VIEW_ON')
    if show_text.vp_info_display_panel:
        
        # Edit mode
        split = layout.split(percentage=0.1)
        split.separator()
        split2 = split.split()
        row = split2.row()       
        row.prop(show_text, "edt_use", text="")
        row.prop(show_text, "edt_options",text="Edit", icon='EDITMODE_HLT') 
        if show_text.edt_options:
            box = layout.box()
            row = box.row(align=True)
            row.prop(show_text, "faces_count_edt")
            row.prop(show_text, "tris_count_edt")            
            row = box.row(align=True)            
            row.prop(show_text, "ngons_count_edt")
            row.prop(show_text, "verts_count_edt")
            row = box.row()
            row.prop(show_text, "edt_corner", expand=True)
            row = box.row(align=True)
            row.prop(show_text, "edt_pos_x")
            row.prop(show_text, "edt_pos_y")
                  
        
        # Object mode
        split = layout.split(percentage=0.1)
        split.separator()
        split2 = split.split()
        row = split2.row() 
        row.prop(show_text, "obj_use", text="")
        row.prop(show_text, "obj_options",text="Object", icon='OBJECT_DATAMODE')
        if show_text.obj_options:
            box = layout.box()
            row = box.row(align=True)
            row.prop(show_text, "faces_count_obj")
            row.prop(show_text, "tris_count_obj")            
            row = box.row(align=True)            
            row.prop(show_text, "ngons_count_obj")
            row.prop(show_text, "verts_count_obj")
            if len(bpy.context.selected_objects) >= 2:
                row = box.row()
                row.prop(show_text, "multi_obj_enabled")
            row = box.row()
            row.prop(show_text, "obj_corner", expand=True)                        
            row = box.row(align=True)
            row.prop(show_text, "obj_pos_x")
            row.prop(show_text, "obj_pos_y")
            
        
        # Sculpt mode
        split = layout.split(percentage=0.1)
        split.separator()
        split2 = split.split()
        row = split2.row() 
        row.prop(show_text, "sculpt_use", text="")
        row.prop(show_text, "sculpt_options",text="Sculpt", icon='SCULPTMODE_HLT')
        if show_text.sculpt_options:
            box = layout.box()
            row = box.row(align=True)           
            row.prop(show_text, "brush_radius")            
            row.prop(show_text, "brush_strength") 
            row = box.row()            
            row.prop(show_text, "symmetry_use")
            row = box.row()
            box.label("Dyntopo fonctions:")
            row = box.row(align=True)             
            row.prop(show_text, "refine_method")
            row.prop(show_text, "detail_type")
            row = box.row()
            row.prop(show_text, "sculpt_corner", expand=True)
            row = box.row(align=True)
            row.prop(show_text, "sculpt_pos_x")
            row.prop(show_text, "sculpt_pos_y")
            
        
        # Render
        split = layout.split(percentage=0.1)
        split.separator()
        split2 = split.split()
        row = split2.row() 
        row.prop(show_text, "rder_use", text="")
        row.prop(show_text, "rder_options",text="Render", icon='CAMERA_DATA')
        if show_text.rder_options:
            box = layout.box()
            row = box.row(align=True)            
            row.prop(show_text, "rder_reso")
            row.prop(show_text, "rder_f_range")
            row = box.row(align=True)
            row.prop(show_text, "rder_f_rate")
            row.prop(show_text, "rder_sample")
            row = box.row()
            row.prop(show_text, "rder_corner", expand=True)
            row = box.row(align=True)
            row.prop(show_text, "rder_pos_x")
            row.prop(show_text, "rder_pos_y")
            
        
        # Scene
        split = layout.split(percentage=0.1)
        split.separator()
        split2 = split.split()
        row = split2.row() 
        row.prop(show_text, "scn_use", text="")
        row.prop(show_text, "scn_options",text="Scene", icon='SCENE_DATA')
        if show_text.scn_options:
            box = layout.box()
            row = box.row(align=True)
            row.prop(show_text, "obj_count")
            row.prop(show_text, "cam_dist")
            row = box.row(align=True)
            row.prop(show_text, "current_frame")
            row.prop(show_text, "cam_focal")
            row = box.row()
            row.prop(show_text, "scn_corner", expand=True)
            row = box.row(align=True)
            row.prop(show_text, "scn_pos_x")
            row.prop(show_text, "scn_pos_y")
            
        
        # Text options
        split = layout.split(percentage=0.1)
        split.separator()
        split2 = split.split()
        split2.prop(show_text, "options_use", text="Options", icon='SCRIPTWIN')
        if show_text.options_use:
            box = layout.box()
            row = box.row()
            row.prop(show_text, "text_font_size")
            row = box.row()
            row.prop(show_text, "name_color")
            row = box.row()
            row.prop(show_text, "label_color")
            row = box.row()
            row.prop(show_text, "value_color")
        
        
    
    