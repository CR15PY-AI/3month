import argparse 
from homework7_DBhelper import DBHelper
def parse_args():
    parser = argparse.ArgumentParser(description = "CRUD CLI для таблицы users")
    sub = parser.add_subparsers(dest = "cmd", required = True)
    p = sub.add_parser("add", help = "Добавить пользователя")
    p.add_argument('--name', required = True, help = "имя")
    p.add_argument('--age', type = int,  required = True, help = 'возраст' )
    p.add_argument("--email", help = "Почта")
    p.add_argument("--skills", help = "Способности")

    sub.add_parser('list', help = "Показать всех пользователей")
    p = sub.add_parser('find', help = "Найти пользователя по ключевому слову")
    p.add_argument('key_word', required=True, help = "Часть имени или почты")

    p = sub.add_parser('update' , help = "обновить данные пользователя")
    p.add_argument('--id', type = int, required=True, help = "ID пользователя")
    p.add_argument('--name', help = "Новое имя")
    p.add_argument('--age', type = int, help = "Новый возраст")
    p.add_argument('--email', help = "Новая почта")
    p.add_argument("--skills", help = "Новые способности")

    p = sub.add_parser('delete', help = "Удалить пользователя по ID")
    p.add_argument('--id', tupe = int, required=True, help = "ID пользователя")

    return parser.parse_args()

def main():
    args = parse_args()
    db = DBHelper()

    if args.cmd == "add":
        uid = db.add_user(args.name, args.age, args.email)
        print(f"пользователь создан с ID: {uid}")
    
    elif args.cmd == "find":
        rows = db.get_all_users() 
        print("ID  |  Name   | Age  |  Email  | Skills ")  
        print("--------------------------------------------------")
        for r in rows:
            print(f"{r['id']:2d} | {r['name']:<10} | {r['age'] or '-':>3} | {r['email'] or '-'} | {r['skills']}")
  
    elif args.cmd == "find":
        rows = db.find_users(args.keyword)
        if rows:
            for r in rows:
                print(f"{r['id']}: {r['name']} ({r['age']}), {r['email']}, {r['skills']}")
        else:
            print("Ничего не найдено")

    elif args.cmd == 'update':
        count = db.update_user(args.id, args.name, args.age, args.email, args.skills)
        if count:
            print(f"Обновленно строк: {count}")
        else:
            print("нечего обновлять или пользователь не найден")
    elif args.cmd == 'delete':
        count = db.delete_user(args.id)
        print(f"Удалено строк: {count}")


if __name__ == '__name__':
    main()