from OCR.OCR import *

global_model = load_model()

def OCR(image_path, thresholding = 160):
    """
        用来连接OCR调用，通过home/views.py来预加载全局模型
        imgae_path 输入图片路径，识别图片为行提取结果
    """
    global global_model
    with K.get_session().graph.as_default():
        out, _ = predict(image_path, global_model, thresholding=thresholding)

    return out

# caffe 模型
# import fp.TextBoxes.detect_textline as dt
# global_caffe_model = dt.load_caffe_model()