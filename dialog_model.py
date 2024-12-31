from transformers import AutoModelForCausalLM, AutoTokenizer


class Dialog:
    def __init__(self):
        # モデルとトークナイザーのロード
        model_name = "rinna/japanese-gpt-neox-3.6b"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.history = []

    def resp_echo(self, user_input_text):
        return f"{user_input_text}"
    
    def generate_response(self, user_input):
        # 会話履歴を更新
        self.history.append(f"ユーザー: {user_input}")
        input_text = "\n".join(self.history)

        # 応答生成
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        output = self.model.generate(
            inputs,
            max_length=512,
            num_return_sequences=1,
            pad_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=2,
            top_p=0.9,
            temperature=0.8
        )

        # 応答をデコード
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        response = response.split("モデル:")[-1].strip()  # 応答部分を抽出

        # 会話履歴を更新
        self.history.append(f"モデル: {response}")
        return response
