def convert_scribd_link(original_link):
    doc_id = original_link.split('/')[-2]
    embed_link = f"https://www.scribd.com/embeds/{doc_id}/content"
    return embed_link

def main():
    original_link = input("Enter the original Scribd link: ")
    embed_link = convert_scribd_link(original_link)
    print(f"Embed link: {embed_link}")
    
    save_option = input("Would you like to save this link to saved.txt? (y/n): ").strip().lower()
    if save_option == 'y':
        with open("saved.txt", "a") as file:
            file.write(embed_link + "\n")
        print("Link saved to saved.txt")
    else:
        print("Link not saved")

if __name__ == "__main__":
    main()
