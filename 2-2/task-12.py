def is_safe_request(messages: list) -> bool:
    # Ваш код здесь
    all_is_dict = all(isinstance(m, dict) and "role" in m and "content" in m for m in messages)

    if not all_is_dict:
        return False

    return any(m["role"] == "system" for m in messages)


def main():
    mmm = [
        {"role": "sdsfsdf", "content": "sdsfsdfs"},
        {"role": "sdsfsdf", "content": "sdsfsdfs"},
        {"role": "sdsfsdf", "content": "sdsfsdfs"},
        {"role": "system", "content": "sdsfsdfs"},
        {"role": "sdsfsdf", "content": "sdsfsdfs"},
        {"role": "sdsfsdf"},
        {"role": "sdsfsdf", "content": "sdsfsdfs"},
    ]

    print(is_safe_request(mmm))


if __name__ == "__main__":
    main()