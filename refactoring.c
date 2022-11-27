#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//최대 이름 길이
#define MAX_NLEN 20

//학생 구조체 정의
typedef struct Student
{
  char name[MAX_NLEN + 1]; //이름
  int score;               // 학생 점수
  int rank;                // 학생 등수
  struct Student *next;    // next
  struct Student *prev;    // prev
} Student;

Student *head, *tail;

void Init(void);  //초기화
void Start(void); // 실행
void End(void);   //종료하기 전에 할당한 메모리 해제

// 각 기능들
int menu(void);             //메뉴 출력,선택지 선택
void AddStudent(void);      //학생 데이터 추가
void RemoveStudent(void);   //학생 데이터 삭제
void FindStudentName(void); //학생 검색

// 메인함수
int main(void)
{
  Init();  //초기화
  Start(); // 실행
  End();   //종료하기 전에 할당한 메모리 해제
  return 0;
}

// 초기화
void Init(void)
{
  head = (Student *)malloc(sizeof(Student)); //머리 더미 노드 생성
  tail = (Student *)malloc(sizeof(Student)); //꼬리 더미 노드 생성
  head->next = tail;                         //맨 앞 머리 더미노드 next를 tail로 설정
  tail->prev = head;                         //맨 뒤 꼬리 더미노드 prev를 head로 설정
  head->prev = tail->next = NULL;            // 머리 이전과 꼬리 다음 노드는 NULL값 저장
}

// 작동 함수
void Start()
{
  // 선택 변수 선언
  int choice = 0;

  // 메뉴판을 불러옴
  // 메뉴가 0이 아니라면 반복해서 실행

  while ((choice = menu()) != 0)
  {
    //선택한 값에 따라 실행
    switch (choice)
    {
    case 1:
      // 학생 입력
      AddStudent();
      break;
    case 2:
      // 학생 제거
      RemoveStudent();
      break;
    case 3:
      // 이름으로 학생 찾기
      FindStudentName();
      break;
    default:
      // 0~3사이의 숫자 입력안할시 아래 문구 출력
      printf("0~3사이의 숫자를 입력해주세요.\n");
      break;
    }
  }
  // 프로그램 종료 문구
  printf("프로그램을 종료합니다\n");
}

// 메뉴 출력
int menu()
{
  // 선택지 받기
  int choice = 0;

  // 메뉴
  printf("---- 성적 관리 프로그램 ----\n");
  printf("1: 학생 데이터 입력\n");
  printf("2: 학생 데이터 삭제\n");
  printf("3: 학생 검색\n");
  printf("0: 종료\n");
  printf("-----------------------------\n");
  printf("입력 : ");
  scanf("%d", &choice);
  // 선택값 반환
  return choice;
}

// 범위 안의 성적인지 체크
int CheckScore(int score) { return (score >= 0) && (score <= 100); }

// 학생추가 함수
void AddStudent()
{
  // stu 노드 생성
  Student *stu = 0;
  stu = (Student *)malloc(sizeof(Student));

  // 이름 입력받기
  printf("이름 : ");
  scanf("%s", stu->name);

  // 성적 입력받기
  printf("성적 : ");
  scanf("%d", &stu->score);
  printf("\n");

  //유효한 성적이 아닐 때
  if (CheckScore(stu->score) == 0)
  {
    //-1저장
    stu->score = -1;
    printf("0~100 사이의 성적을 입력해주시길 바랍니다.\n 그 외의 숫자를 입력하여 성적이 -1로 처리되었습니다.\n");
  }

  //새로 생성한 노드 tail 앞에 달기
  stu->next = tail;
  stu->prev = tail->prev;
  tail->prev->next = stu;
  tail->prev = stu;

  //학생 등수 먹이기
  stu->rank = 0; // 기본 등수 0등

  // 화살표 노드
  Student *seek;
  // 생성된 노드 반복문으로 하나씩 보기
  for (seek = head->next; seek != tail; seek = seek->next)
  {
    // 새로 추가된 점수가 현재 노드의 점수보다 작다면 새로 추가될 점수의 등수 증가 시킴
    if (stu->score < seek->score)
    {
      stu->rank++;
    }
    else
    { // 그 외에는 현재 노드의 등수 증가 시킴
      seek->rank++;
    }
  }
}

// 학생제거
void RemoveStudent()
{
  // 이름 변수
  char name[MAX_NLEN + 1];
  // seek 선언
  Student *seek;

  // 삭제할 학생 이름 입력받기
  printf("삭제할 학생 이름: ");
  scanf("%s", name);

  //전체 노드 탐색
  for (seek = head->next; seek != tail; seek = seek->next)
  {

    // 해당 노드와 Name이 같다면 이를 제거
    if (!strcmp(seek->name, name))
    {
      //연결리스트에서 링크 조절
      seek->prev->next = seek->next;
      seek->next->prev = seek->prev;

      // 삭제 후 할당 해제 이전에 전체 등수 정보 업데잍트
      Student *stu;
      for (stu = head->next; stu != tail; stu = stu->next)
      {
        // 새로 추가된 점수가 현재 노드의 점수보다 작다면 새로 추가될 점수의 등수 증가 시킴
        // seek는 삭제될 노드
        if (stu->score < seek->score)
        {
          stu->rank--;
        }
        else
        { // 그 외에는 등수변동없음
          continue;
        }
      }
      free(seek); //메모리 해제

      printf("삭제하였습니다.\n");
      return;
    }
  }
  // 만약 없는 데이터라면
  printf("데이터가 없습니다.\n");
}

// 학생 찾기 : 이름을 통해서
void FindStudentName()
{
  // 이름, seek선언
  char name[20] = "";
  Student *seek = 0;

  // 이름 입력받기
  printf("검색할 학생 이름: ");
  scanf("%s", name);

  // 반복문 돌기
  for (seek = head->next; seek != tail; seek = seek->next)
  {
    // 문자열 비교, 같은 이름 찾으면 출력
    if (!strcmp(seek->name, name))
    {
      // 해당 학생 점수, 등수 출력
      printf("학생 점수 : %d \n", seek->score);
      printf("학생 등수 : %d \n", seek->rank);
      printf("\n");
      return; // 프로그램 종료
    }
  }

  // 위에서 데이터 못찾을시 데이터 없음 문구 출력
  printf("데이터가 없습니다.\n");
}

//  종료
void End()
{
  Student *seek = head;
  // node 할당해제
  while (seek->next)
  {
    seek = seek->next;
    free(seek->prev);
  }
  // seek 할당해제
  free(seek);
}
