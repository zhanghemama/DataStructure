#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Array
{
    int size;
    int used;
    int * arr;
};

void dump(struct Array * array)
{
    for (int index = 0; index < array->used; index++)
    {
        printf("[%02d]: %08d\n", index, array->arr[index]);
    }
}

void alloc(struct Array* array)
{
    array->arr = (int*)malloc(array->size * sizeof(int));
}

int insert(struct Array* array, int element)
{
    if (array->used >= array->size)
    {
        return -1;
    }
    
    int index = 0;
    for (; index < array->used; index++)
    {
        if (array->arr[index] > element)
        {
            break;
        }
    }
    
    if (index < array->used)
    {
        memmove(&array->arr[index + 1], &array->arr[index], sizeof(int) * (array->used - index));
    }
    
    array->arr[index] = element;
    array->used++;
    
    return index;
}

int delete(struct Array* array, int index)
{
    if (index >= array->used)
    {
        return -1;
    }
    
    memmove(&array->arr[index], &array->arr[index+1], sizeof(int) * (array->used - index - 1));
    array->used--;
    
    return 0;
}

int search(struct Array* array, int element)
{
    int index = 0;
    for (; index < array->used; index++)
    {
        if (array->arr[index] == element)
        {
            return index;
        }
        
        if (array->arr[index] > element)
        {
            return -1;
        }
    }
    
    return -1;
}

int main(int argc, const char * argv[]) {
    
    int idx;
    struct Array ten_int = {10, 0, NULL};
    
    alloc(&ten_int);
    if (!ten_int.arr)
        return -1;
    insert(&ten_int, 1);
    insert(&ten_int, 3);
    insert(&ten_int, 2);
    printf("=== insert 1, 3, 2\n");
    dump(&ten_int);
    
    idx = search(&ten_int, 2);
    printf("2 is at position %d\n", idx);
    idx = search(&ten_int, 9);
    printf("9 is at position %d\n", idx);
    
    printf("=== delete [6] element \n");
    delete(&ten_int, 6);
    dump(&ten_int);
    printf("=== delete [0] element \n");
    delete(&ten_int, 0);
    dump(&ten_int);
    
    return 0;
}
