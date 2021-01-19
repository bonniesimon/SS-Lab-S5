#include <stdio.h>
//#include<conio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 10

void swap(char *x, char *y)
{
    char t = *x;
    *x = *y;
    *y = t;
}
void reverse(char str[], int length)
{
    int start = 0;
    int end = length - 1;
    while (start < end)
    {
        swap((str + start), (str + end));
        start++;
        end--;
    }
}
char *itoa(int num, char *str, int base)
{
    int i = 0;
    int isNegative = 0;
    if (num == 0)
    {
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }
    if (num < 0 && base == 10)
    {
        isNegative = 1;
        num = -num;
    }

    while (num != 0)
    {
        int rem = num % base;
        str[i++] = (rem > 9) ? (rem - 10) + 'a' : rem + '0';
        num = num / base;
    }
    if (isNegative)
        str[i++] = '-';

    str[i] = '\0';

    reverse(str, i);

    return str;
}
void string2hexString(char *input, char *output)
{
    int loop;
    int i;

    i = 0;
    loop = 2;

    while (loop < strlen(input) - 1)
    {
        sprintf((char *)(output + i), "%02X", input[loop]);
        loop += 1;
        i += 2;
    }
    output[i++] = '\0';
}

void main()
{
    FILE *inp, *namtab, *deftab, *argtab, *output;
    int len, i, pos = 1;
    char arg[20], mne[20], opnd[20], label[20], name[20], mne1[20], opnd1[20], pos1[10], pos2[10];
    //clrscr();
    inp = fopen("input.txt", "r");
    namtab = fopen("namtab.txt", "w+");
    deftab = fopen("deftab.txt", "w+");
    argtab = fopen("argtab.txt", "w+");
    output = fopen("op.txt", "w+");
    fscanf(inp, "%s%s%s", label, mne, opnd);
    while (strcmp(mne, "END") != 0)
    {
        if (strcmp(mne, "MACRO") == 0)
        {
            fprintf(namtab, "%s\n", label);
            fseek(namtab, SEEK_SET, 0);
            fprintf(deftab, "%s\t%s\n", label, opnd);
            fscanf(inp, "%s%s%s", label, mne, opnd);
            while (strcmp(mne, "MEND") != 0)
            {
                if (opnd[0] == '&')
                {
                    itoa(pos, pos1, 5);
                    strcpy(pos2, "?");
                    strcpy(opnd, strcat(pos2, pos1));
                    pos = pos + 1;
                }
                fprintf(deftab, "%s\t%s\n", mne, opnd);
                fscanf(inp, "%s%s%s", label, mne, opnd);
            }
            fprintf(deftab, "%s", mne);
        }
        else
        {
            fscanf(namtab, "%s", name);
            if (strcmp(mne, name) == 0)
            {
                len = strlen(opnd);
                for (i = 0; i < len; i++)
                {
                    if (opnd[i] != ',')
                        fprintf(argtab, "%c", opnd[i]);
                    else
                        fprintf(argtab, "\n");
                }
                fseek(deftab, SEEK_SET, 0);
                fseek(argtab, SEEK_SET, 0);
                fscanf(deftab, "%s%s", mne1, opnd1);
                fprintf(output, ".\t%s\t%s\n", mne1, opnd);
                fscanf(deftab, "%s%s", mne1, opnd1);
                while (strcmp(mne1, "MEND") != 0)
                {
                    if ((opnd[0] == '?'))
                    {
                        fscanf(argtab, "%s", arg);
                        fprintf(output, "-\t%s\t%s\n", mne1, arg);
                    }
                    else
                        fprintf(output, "-\t%s\t%s\n", mne1, opnd1);
                    fscanf(deftab, "%s%s", mne1, opnd1);
                }
            }
            else
                fprintf(output, "%s\t%s\t%s\n", label, mne, opnd);
        }
        fscanf(inp, "%s%s%s", label, mne, opnd);
    }
    fprintf(output, "%s\t%s\t%s", label, mne, opnd);
    fclose(inp);
    fclose(namtab);
    fclose(deftab);
    fclose(argtab);
    fclose(output);
    printf("files to be viewed \n");
    printf("1. argtab.txt\n");
    printf("2. namtab.txt\n");
    printf("3. deftab.txt\n");
    printf("4. op.txt\n");
    //getch();
}