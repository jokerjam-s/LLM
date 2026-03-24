def truncate_prompt(text: str, max_length: int) -> str:
    # Ваш код здесь
    if len(text) <= max_length:
        return text

    space_pos = text.rfind(' ')
    while space_pos > max_length:
        space_pos = text.rfind(' ', 0, space_pos)

    return f"{text[:space_pos]}..." if space_pos > 0 else '...'


def main():
    txt = "ssdf sfsdfs sdfsd sgfgfhg iopoiu uyiyui iyuiyui"
    print(truncate_prompt(txt, 55))
    print(truncate_prompt(txt, 5))
    print(truncate_prompt(txt, 15))
    print(truncate_prompt(txt, 4))
    print(truncate_prompt(txt, 2))


if __name__ == "__main__":
    main()
