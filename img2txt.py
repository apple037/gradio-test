import gradio as gr
import replicate
import os
from dotenv import load_dotenv
import base64
from PIL import Image

load_dotenv()
api_key = os.getenv("REPLICATE_API_KEY")
client = replicate.Client(api_token=api_key)

# 定義輸入介面
def parse_image(image_url):
    # 使用 Replicate 套件呼叫模型
    result = client.run(
        "andreasjansson/blip-2:4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608",
        input={"image": image_url}
    )

    return result


def main():
    # 定義 Gradio app
    inputs = gr.inputs.Textbox(label="輸入圖片 URL")
    outputs = gr.outputs.Textbox(label="圖片解析結果")
    app = gr.Interface(
        fn=parse_image,
        inputs=inputs,
        outputs=outputs,
        title="Blip2 圖片解析器",
        description="輸入圖片 URL，Blip2 模型將解析其內容。"
    )

    # 啟動 Gradio app
    app.launch()


if __name__ == "__main__":
    main()
