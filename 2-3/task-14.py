
class LLMFactory:
    @staticmethod
    def create(provider: str):
        # пишите ваш код тут
        if provider in ("openai", "ollama"):
            return LLMFactory()
        else:
            raise ValueError

    def generate(self, message: list):
        return "mocked response"