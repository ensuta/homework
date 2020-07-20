#include <stdio.h>


int main() 

{
	int num, way, num2, con;
     printf("첫 숫자를 입력하시오\n");

	scanf( "%d",&num);
    printf("계산 방식 + - x / \n");
    scanf("%d", &way);
	printf(" 두번째 숫자 입력. 전의 숫자 [%d]\n", num);
    scanf("%d",&num2);
    if(way==1) con=num+num2;
    else if(way==2) con=num-num2;
    else if(way==3) con=num*num2;
    else if(way==4)  con=num/num2;
    printf("결과 \n %d",con);
    
	
	return 0;

}
