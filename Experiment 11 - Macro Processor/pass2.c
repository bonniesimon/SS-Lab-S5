#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void main()
{
    FILE *inp, *namtab, *deftab, *argtab, *output;
    int i, len;
    char mne[20], opnd[20], label[20], name[20], mne1[20], opnd1[20], arg[20];
    inp = fopen("inp.txt", "r");
    namtab = fopen("namtab.txt", "r");
    deftab = fopen("deftab.txt", "r");
    argtab = fopen("argtab.txt", "w+");
    output = fopen("op2.txt", "w");
    fscanf(inp, "%s%s%s", label, mne, opnd);
    while (strcmp(mne, "END") != 0)
    {
        // Skipping the Macro definition in this pass (cuz we already parsed it)
        if (strcmp(mne, "MACRO") == 0)
        {
            fscanf(inp, "%s%s%s", label, mne, opnd);
            while (strcmp(mne, "MEND") != 0)
                fscanf(inp, "%s%s%s", label, mne, opnd);
        }
        else
        {
            // checking if menmonic is present in namtab, ie if mne is a macro invocation
            //          else write directly to output
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
                fseek(namtab, SEEK_SET, 0);
                fseek(argtab, SEEK_SET, 0);
                // Writing from deftab to output
                fscanf(deftab, "%s%s", mne1, opnd1);
                fprintf(output, ".\t%s\t%s\n", mne1, opnd);
                fscanf(deftab, "%s%s", mne1, opnd1);
                while (strcmp(mne1, "MEND") != 0)
                {
                    if ((opnd1[0] == '&'))
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
    fprintf(output, "%s\t%s\t%s\n", label, mne, opnd);
    fclose(inp);
    fclose(namtab);
    fclose(deftab);
    fclose(argtab);
    fclose(output);
    printf("pass is completed\n");
}