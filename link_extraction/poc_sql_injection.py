import extract_links_with_validation
import pandas as pd

def main():
    links = extract_links_with_validation.get_internal_links()

    df = pd.DataFrame(links)
    print(df)

    # print(f"internal links are: {links}")

if __name__ == '__main__':
    main()
