from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine("postgres://postgres:b4ah6z1532@localhost:5432/Pdf_to_Text")
db = scoped_session(sessionmaker(bind=engine))

def main(text):
    db.execute(f"INSERT INTO TextHighlight(Text) VALUES(:text)",{"text":text})
    print(f"added {text}")
    db.commit()

if __name__ == "__main__":
    x = input("Enter a word:  ")
    main(x)


