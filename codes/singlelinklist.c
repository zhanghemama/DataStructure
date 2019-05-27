#include <stdio.h>
#include <stdbool.h>

struct single_list
{
    struct single_list * next;
    int value;
};

struct single_list_head
{
    struct single_list * head;
};

bool is_empty(struct single_list_head* head)
{
    if (head && head->head)
    {
        return false;
    }
    return true;
}

void dump(struct single_list_head* head)
{
    if (is_empty(head))
    {
        return;
    }
    
    struct single_list* list = head->head;
    int index = 0;
    while (list)
    {
        printf("[%02d] : [%08d]\n", index, list->value);
        list = list->next;
        index++;
    }
}

int insert(struct single_list** prev, struct single_list* element)
{
    if (!prev || !element)
    {
        return -1;
    }
    
    element->next = *prev;
    *prev = element;
    
    return 0;
}

int insert_head(struct single_list_head* head, struct single_list* element)
{
    if (!head)
    {
        return -1;
    }
    return insert(&head->head, element);
}

struct single_list* delete(struct single_list** prev)
{
    if (!prev)
    {
        return NULL;
    }
    
    struct single_list* tmp = *prev;
    *prev = (*prev)->next;
    tmp->next = NULL;
    
    return tmp;
}

struct single_list* delete_head(struct single_list_head* head)
{
    if (is_empty(head))
    {
        return NULL;
    }
    
    return delete(&head->head);
}

struct single_list** search(struct single_list_head* head, int element)
{
    if (is_empty(head))
    {
        return NULL;
    }
    
    struct single_list** prev = &head->head;
    struct single_list* list = *prev;

    while (list)
    {
        if (list->value >= element)
        {
            break;
        }

        prev = &list->next;
        list = *prev;
    }
    return prev;
}

struct single_list* middle(struct single_list_head* head)
{
    if (is_empty(head))
    {
        return NULL;
    }
    
    struct single_list* s1 = head->head;
    struct single_list* s2 = s1;
    
    while (true)
    {
        if (!s2 || !s2->next)
        {
            return s1;
        }
        
        s1 = s1->next;
        s2 = s2->next->next;
    }
    
    return NULL;
}

void reverse(struct single_list_head* head)
{
    if (is_empty(head))
    {
        return;
    }
    
    struct single_list_head tmp;
    struct single_list* element = NULL;
    
    while (!is_empty(head))
    {
        element = delete_head(head);
        insert_head(&tmp, element);
    }
    
    head->head = tmp.head;
}

bool is_cyclic(struct single_list_head* head)
{
    if (is_empty(head))
    {
        return false;
    }
    
    struct single_list* slow = head->head;
    struct single_list* fast = slow;
    struct single_list* pre = NULL;
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        struct single_list* next = slow->next;
        slow->next = pre;
        pre = slow;
        slow = next;
    }
    
    if (fast)
    {
        slow = slow->next;
    }
    
    while (pre && slow)
    {
        if (pre->value != slow->value)
        {
            return false;
        }
        pre = pre->next;
        slow = slow->next;
    }
    
    return true;
}

int main(int argc, const char * argv[])
{
    // insert code here...
    struct single_list_head head = {NULL};
    struct single_list lists[10];
    struct single_list **prev;
    int index = 0;
    
    for (index = 0; index < 10; index++)
    {
        if (index >= 5)
        {
            lists[index].value = index - 5;
        }
        else
        {
            lists[index].value = index;
        }
        lists[index].next = NULL;
    }
    
    insert_head(&head, &lists[5]);
    insert_head(&head, &lists[6]);
    insert_head(&head, &lists[8]);
    insert_head(&head, &lists[9]);
    insert_head(&head, &lists[4]);
    insert_head(&head, &lists[3]);
    insert_head(&head, &lists[1]);
    insert_head(&head, &lists[0]);
    
    printf("=== insert 0, 1\n");
    dump(&head);
    
    prev = search(&head, 2);
    insert(prev, &lists[2]);
    printf("=== insert 2\n");
    dump(&head);
    
    printf("middle elem is %d\n", middle(&head)->value);

    prev = search(&head, 2);
    if ((*prev) && ((*prev)->value == 2))
        printf("The list contains 2\n");
    else
        printf("The list not contains 2\n");
    
    delete(prev);
    prev = search(&head, 2);
    printf("After remove 2\n");
    if ((*prev) && ((*prev)->value == 2))
        printf("The list contains 2\n");
    else
        printf("The list not contains 2\n");
    dump(&head);
    
    printf("After reverse \n");
    reverse(&head);
    dump(&head);
    
    printf("middle elem is %d\n", middle(&head)->value);

    printf("link is cyclic %d\n", is_cyclic(&head));
    return 0;
}
