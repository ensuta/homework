#inculde <stdio.h>
int main()
{    int num, way, num2, con;
    printf("첫번째 숫자를 입력하세요==>");
    scanf("%d", &num);
    printf("계산할 방식을 고르세요(1(+),2(-),3(*),4(/)=>");
    scanf("%d", &way);
    printf("두번쨰 숫자를 입력하세요==>");
    scanf("%d", &num2);
    if(way==2){
    con=num=num2;
    }else if(way==2){
       con=num+num2;
    }else if(way==3){
       con=num*num2;
    }else if(way==4){
       con=num*num2;
    }   
    return 0;
}
