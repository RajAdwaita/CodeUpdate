# from sys import maxsize


# def newStack():
#     stack = []
#     return stack


# def isEmpty(stack):
#     return len(stack) == 0


# def pushITEM(stack, item):
#     if (len(stack) > 10):
#         print("Overflow")

#     else:
#         stack.append(item)
#         print(stack)


# def pop_ele(stack):
#     if(isEmpty(stack)):
#         return ("Underflow")
#     (stack.pop())
#     return stack


# print("\\1.push.\\2.pop.\\-1.Exit")
# stack = newStack()
# i = 0
# while(i != -1):
#     i = int(input())

#     if i == 1:
#         pushITEM(stack, ((input())))
#     elif i == 2:
#         print(pop_ele(stack))

#     elif i == -1:
#         exit()

#     else:
#         print("Invalid Choice")
# include <stdio.h>
# include <stdlib.h>
# include <string.h>


# include <stdio.h>
# include <stdlib.h>
# include <string.h>
int main()
{
    char uname[30]
    char pass[20]
    char cpass[20]
    char sec_que[40]
    char sec_ans[40]
    char mobno[11]
    int flag = 0
    int ch = 0

    int rs
    char reset[20]
    char dom[] = "@strangemail.com"
    char ans[20]


    printf("REGISTER: \n")

    printf("Create Account:\n ")

    printf("Enter UserName: ")
    gets(uname)
    strcat(uname, dom)
    printf("Enter Password: ")
    gets(pass)

    while (flag == 0)
    {
        printf("Re-Enter Password: ")
        gets(cpass)

        if (strcmp(cpass, pass) == 0)
        {
            flag = 1
        }
        else
        {
            flag = 0
        }
    }

    printf("Enter Security Question: ")
    gets(sec_que)
    printf("Enter Security Answer: ")
    gets(sec_ans)

    printf("Enter Mobile Number: ")
    gets(mobno)

    printf("Log in: \n")

    char username[30]
    char password[20]
    int tem = 0


    while(ch == 0)
    {
        while(tem == 0){
            printf("Enter UserName: ")
            gets(username)

            if (strcmp(username, uname) == 0)
            {
                tem = 1
            }
            else{
                printf("Wrong username:\n")
                tem = 0
            }

        }


        printf("Enter Password: ")
        gets(password)

        if (strcmp(password, pass) == 0)
        {

            puts(username)
            puts(pass)
            puts(sec_que)
            puts(sec_ans)
            printf("%d", mobno)
            ch = 1
        }

        else
        {
            printf("Wrong Password..Answer security question: \n")

            puts(sec_que)
            printf("Enter new password:  ")
            gets(ans)

            if (strcmp(ans, sec_ans) == 0)
            {

                gets(reset)
                strcpy(pass, reset)
                ch = 0
            }



        }

    }
    return 0
}
