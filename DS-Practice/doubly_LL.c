

// Doubly Linked List Program

#include <stdio.h>
#include <stdlib.h>

struct Node{
  int data;
  struct Node *prev;
  struct Node *next;
};

void appendDLL(struct Node **st, int data){

  struct Node *pNew, *pPre;
  pNew = pPre = *st;

  pNew = (struct Node*)malloc(sizeof(struct Node));
  pNew->data = data;

  if (*st == NULL){
    pNew->prev = NULL;
    *st = pNew;
  }
  else{
    while(pPre->next != NULL){
      pPre = pPre->next;
    }
    pPre->next = pNew;
    pNew->prev = pPre;
  }
  pNew->next = NULL;

}

void displayDLL(struct Node *st){

  while(st != NULL){
    printf("%d <-> ", st->data);
    st = st->next;
  }
  printf("NULL\n");

}
 
void deleteDLL(struct Node **st, int dataout){

  struct Node *pDlt = NULL, *pPre = NULL, *pSucc = *st;
  

  while (pSucc->data != dataout){
    pPre = pSucc;
    pSucc = pSucc->next;
  } 
  pDlt = pSucc;
  pSucc = pDlt->next;

  if (pPre == NULL){
    *st = pDlt->next;
  }
  else if (pSucc == NULL){
    pPre->next = pDlt->next;    
  }
  else{
    pPre->next = pSucc;
    pSucc->prev = pPre;
  }
  free(pDlt);
}

int main(void) {

  printf("Doubly linked list program\n");

  struct Node *start = NULL;

  appendDLL(&start, 10);
  appendDLL(&start, 20);
  appendDLL(&start, 30);
  appendDLL(&start, 40);
  appendDLL(&start, 50);

  displayDLL(start);

  deleteDLL(&start, 50);

  displayDLL(start);

  return 0;
}