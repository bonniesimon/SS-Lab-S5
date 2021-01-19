#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    FILE *inp, *optab, *symtab, *symtab1, *output;
    int locctr, start, i = 0, j = 0, m[10], pgmlen, len, k, len1, l = 0;
    char name[10], opnd[10], label[10], mne[10], s1[10], opcode_mne[10], opcode_addr[10];
    char lcs[10], ms[10];
    char sym[10], symaddr[10], obj1[10], obj2[10], s2[10], q[10], s3[10];
    inp = fopen("input.txt", "r");
    optab = fopen("optab.txt", "r");
    symtab = fopen("symtab_self.txt", "w+");
    symtab1 = fopen("symtab1_self.txt", "w+");
    output = fopen("output_self.txt", "w+");
    fscanf(inp, "%s%s%s", label, mne, opnd);
    if (strcmp(mne, "START") == 0)
    {
        start = atoi(opnd);
        strcpy(name, label);
        locctr = start;
    }
    strcpy(s1, "*");
    fscanf(inp, "%s%s%s", label, mne, opnd);
    while (strcmp(mne, "END") != 0)
    {
        if (strcmp(label, "-") == 0)
        {
            fscanf(optab, "%s%s", opcode_mne, opcode_addr);
            while (!feof(optab))
            {
                if (strcmp(opcode_mne, mne) == 0)
                {
                    m[i] = locctr + 1;
                    fprintf(symtab, "%s\t%s\n", opnd, s1);
                    fprintf(output, "%s\t0000\n", opcode_addr);
                    locctr = locctr + 3;
                    i = i + 1;
                    break;
                }
                else
                    fscanf(optab, "%s%s", opcode_mne, opcode_addr);
            }
        }

        else
        {
            fseek(symtab, SEEK_SET, 0);
            fscanf(symtab, "%s%s", sym, symaddr);
            while (!feof(symtab))
            {
                if (strcmp(sym, label) == 0)
                {
                    sprintf(lcs, "%d", locctr);
                    fprintf(symtab1, "%s\t%s\n", label, lcs);
                    sprintf(ms, "%d", m[j]);
                    j = j + 1;
                    fprintf(output, "%s\t%s\n", ms, lcs);
                    i = i + 1;
                    break;
                }
                else
                    fscanf(symtab, "%s%s", sym, symaddr);
            }
            if (strcmp(mne, "RESW") == 0)
                locctr = locctr + 3 * atoi(opnd);
            else if (strcmp(mne, "BYTE") == 0)
            {
                strcpy(s2, "-");
                len = strlen(opnd);
                locctr = locctr + len - 2;
                for (k = 2; k < len; k++)
                {
                    q[l] = opnd[k];
                    l = l + 1;
                }
                fprintf(output, "%s\t%s\n", q, s2);
                break;
            }
            else if (strcmp(mne, "RESB") == 0)
                locctr = locctr + atoi(opnd);
            else if (strcmp(mne, "WORD") == 0)
            {
                strcpy(s3, "#");
                locctr = locctr + 3;
                fprintf(output, "%s\t%s\n", opnd, s3);
                break;
            }
        }

        fseek(optab, SEEK_SET, 0);
        fscanf(inp, "%s%s%s", label, mne, opnd);
    }
    fseek(output, SEEK_SET, 0);
    pgmlen = locctr - start;
    printf("H^%s^%d^0%x\n", name, start, pgmlen);
    printf("T^");
    printf("00%d^0%x", start, pgmlen);
    fscanf(output, "%s%s", obj1, obj2);
    while (!feof(output))
    {
        if (strcmp(obj2, "0000") == 0)
            printf("^%s%s", obj1, obj2);
        else if (strcmp(obj2, "-") == 0)
        {
            printf("^");
            len1 = strlen(obj1);
            for (k = 0; k < len1; k++)
                printf("%d", obj1[k]);
        }
        else if (strcmp(obj2, "#") == 0)
        {
            printf("^");
            printf("%s", obj1);
        }
        fscanf(output, "%s%s", obj1, obj2);
    }
    fseek(output, SEEK_SET, 0);
    fscanf(output, "%s%s", obj1, obj2);
    while (!feof(output))
    {
        if (strcmp(obj2, "0000") != 0)
        {
            if (strcmp(obj2, "-") != 0)
            {
                if (strcmp(obj2, "#") != 0)
                {
                    printf("\n");
                    printf("T^%s^02^%s", obj1, obj2);
                }
            }
        }
        fscanf(output, "%s%s", obj1, obj2);
    }
    printf("\nE^00%d\n", start);
}