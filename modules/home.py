import streamlit

def choose() -> str:
    with streamlit.form("choose_market"):
        option = streamlit.selectbox(
            "Choose a market: ",
            ["Yogendra Labs", "Falconex Networks Inc", "Hyperion Invest X", "Veridium Corp", "Zenthic Innovations"],
        )
        submit_button = streamlit.form_submit_button(label="Submit")
    return str(option) if submit_button else ""

def main(user):
    option = choose()
    match option:
        case "Yogendra Labs":
            
            pass
        case "Falconex Networks Inc":
            pass
        case "Hyperion Invest X":
            pass
        case "Veridium Corp":
            pass
        case "Zenthic Innovations":
            pass

if __name__ == "__main__":
    main()
