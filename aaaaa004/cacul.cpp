
#include <stdio.h>

int main()
{
    while(1){
        int num,how,num2,con;
        char wor;
    printf("계산 할 숫자를 입력하세요");
    scanf("%d",&num);
    printf("계산할 방식을 고르시오(+(1),-(2),*(3),/(4)");
    scanf("%d",&how);
    printf("다시 계산 할 숫자를 입력하세요");
    scanf("%d",&num2);
    if(how==1){
        con=num+num2;
        wor='+';
    }else if(how==2){
        con=num-num2;
        wor='-';
    }else if(how==3){
        con=num*num2;
        wor='*';
    }else if(how==4){
        con=num/num2;
        wor='/';
    }else if(how==0){
        break;
    }
    printf("%d %c %d= %d \n",num,wor,num2,con);
}
    return 0;
}
