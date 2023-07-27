# 参考代码1：使用gradio实现可视化的演示系统。
import gradio as gr
import cv2

# -------------------function------------------
# 只要修改这个函数内部的内容就可以输出想要的内容
def my_function(image):
    output = cv2.resize(image, (100, 100)) # 这里利用cv2工具实现了对图像的尺寸变换。可以在这里进行图像处理，如提取关键点等。
    return output,type(output)
# -------------------function------------------

interface = gr.Interface(fn=my_function, inputs="image", outputs=['image','text'])
interface.launch(share=True)
