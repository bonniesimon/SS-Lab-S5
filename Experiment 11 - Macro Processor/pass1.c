#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void main()
{
    FILE *inp, *namtab, *deftab;
    char mne[20], opnd[20], label[20];
    inp = fopen("inp.txt", "r");
    namtab = fopen("namtab.txt", "w+");
    deftab = fopen("deftab.txt", "w+");
    fscanf(inp, "%s%s%s", label, mne, opnd);
    while (strcmp(mne, "MEND") != 0)
    {
        if (strcmp(mne, "MACRO") == 0)
        {
            fprintf(namtab, "%s\n", label);
            fprintf(deftab, "%s\t%s\n", label, opnd);
        }
        else
            fprintf(deftab, "%s\t%s\n", mne, opnd);
        fscanf(inp, "%s%s%s", label, mne, opnd);
    }
    fprintf(deftab, "%s", mne);
    fclose(inp);
    fclose(namtab);
    fclose(deftab);
    printf("Pass 1 is completed\n");
}