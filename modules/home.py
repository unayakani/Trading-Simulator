import streamlit

def choose() -> str:
    with streamlit.form("choose_market"):
        option = streamlit.selectbox(
                "Choose a market: ",
                ["Yogendra Labs"],
        )
    return str(option)

def main():
    option = choose()
    match option:
        case "Yogendra Labs":
            pass
        case "a":
            pass
        case "b":
            pass
        case "c":
            pass
        case "d":
            pass
