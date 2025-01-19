import cv2
import streamlit as st
from deep_list import *
import torch

def main():
    st.title("Dashboard")
    inference_msg = st.empty()
    st.sidebar.title("Configuration")

    input_source = st.sidebar.radio(
     "Select input source",
     ('CCTV Feed', 'Local video'))

    conf_thres = st.sidebar.text_input("Class confidence threshold", "0.55")

    conf_thres_drift = st.sidebar.text_input("Class confidence threshold for drift dectection", "0.70")

    fps_drop_warn_thresh = st.sidebar.text_input("FPS drop warning threshold", "8")

    save_output_video = st.sidebar.radio("Save output video?",('Yes', 'No'))
    if save_output_video == 'Yes':
        nosave = False
        display_labels = False
    else:
        nosave = True
        display_labels = True
    
    save_poor_frame = st.sidebar.radio("Save poor performing frames?",('Yes', 'No'))
    if save_poor_frame == "Yes":
        save_poor_frame__ = True
    else:
        save_poor_frame__ = False
    
    # ------------------------- LOCAL VIDEO ------------------------------
    if input_source == "Local video":
        video = st.sidebar.file_uploader("Select input video", type=["mp4", "avi"], accept_multiple_files=False)
        
        if st.sidebar.button("Start tracking"):
    
            stframe = st.empty()

            #st.subheader("Inference Stats")
            #kpi1, kpi2, kpi3 = st.columns(3)

            #st.subheader("System Stats")
            #js1, js2, js3 = st.columns(3)

            # Updating Inference results
            
            #with kpi1:
                #.markdown("**Frame Rate**")
                #kpi1_text = st.markdown("0")
                #fps_warn = st.empty()
            
            #with kpi2:
                #st.markdown("**Detected objects in curret Frame**")
                #kpi2_text = st.markdown("0")
            
            #with kpi3:
                #st.markdown("**Total Detected objects**")
                #kpi3_text = st.markdown("0")
            
            # Updating System stats
            
            #with js1:
                #st.markdown("**Memory usage**")
                #js1_text = st.markdown("0")

            #with js2:
                #st.markdown("**CPU Usage**")
                #js2_text = st.markdown("0")

            #with js3:
                #st.markdown("**GPU Memory Usage**")
                #js3_text = st.markdown("0")

            #st.subheader("Inference Overview")
            #inf_ov_1, inf_ov_2, inf_ov_3, inf_ov_4 = st.columns(4)

            #with inf_ov_1:
                #st.markdown("**Poor performing classes (Conf < {0})**".format(conf_thres_drift))
                #inf_ov_1_text = st.markdown("0")
            
            #with inf_ov_2:
                #st.markdown("**No. of poor peforming frames**")
                #inf_ov_2_text = st.markdown("0")
            
            #with inf_ov_3:
                #st.markdown("**Minimum FPS**")
                #inf_ov_3_text = st.markdown("0")
            
            #with inf_ov_4:
                #st.markdown("**Maximum FPS**")
                #inf_ov_4_text = st.markdown("0")
           
            detect(source=video.name, stframe=stframe, conf_thres=float(conf_thres), nosave=nosave, display_labels=display_labels, conf_thres_drift = float(conf_thres_drift), save_poor_frame__= save_poor_frame__)

            inference_msg.success("Detection Complete!")
            
  
    # torch.cuda.empty_cache()

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
