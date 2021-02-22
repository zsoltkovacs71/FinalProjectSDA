Aplicatia este gandita sa fie folosita de catre o agentie de recrutare.

Agentia poate posta pozitiile aflate in recrutare. Acest lucru se permite in prima faza doar daca un utilizator s-a logat 
folosind meniul Admin. Tot asa pentru a modifica sau a sterge o pozitie aflata in recrutare trebuie sa fie logat utilizatorul.
In functie de prioritati, fiecare pozitie poate fi marcat daca sa fie promovat sau nu.
Astfel primele 4 pozitii care apar pe ecran vor fi selectate dintre cele promovate (random) care vor aparea astfel de 
doua ori in lista de pozitii.

Vizitatorii site-ului pot aplica la pozitiile dorite si in acest pas vor fi obligati sa-si incarce si un CV actual la fiecare aplicare separat.

In pagina este integrat si o functie de cautare care cauta in urmatoarele fielduriÉ
- numele companiei care angajeaza
- denumire pozitiei
- descriere jobului
Folosind aceasta functie vizitatorii pot cauta pozitii in functie de companiile, tehnologiile si frameworkurile de interes pentru ei.


Faza 2.
Ulterior as dori sa implementez si un signup form. Astfel vizitatorii isi pot crea cont unde sa-si incarce CV-ul si la 
aplicare sa nu li se solicite acest lucru.
Cand ajung in aceasta faza va trebui sa schimb drepturile de creare, stergere si modificare pozitii care in faza initiala sunt conditionate de login.


URL-uri faza 1

Acasa - va fi o pagina in care foarte pe scurt se prezinta compania.

Pozitii deschise - face display la pozitiile aflate in recrutare. Lista incepe cu 4 pozitii promovate. 
                 Aici va fi folosit modelul Pozitie. Daca utilizatorul este logat are dreptul sa modifice sau sa stearga o pozitie.
                 Aici vor putea vizitatorii sa aplice la o anumita pozitie. Si aici va fi folosit un form.

Contact - in cazul in care vreun vizitator doresta sa comunice ceva.

Admin - este punctul de meniu in care cei care au drepturi de a posta, modifica si sterge pozitii se pot loga.

Creare pozitii - Aici pot fi create pozitiile. Am integrat un editor de text si astfel fiecare descriere poate fi personalizat 
                 in functie de interese.

Cauta - aici vizitatorii pot cauta companii, pozitii sau tehnologii de interes.

Politica de confidentialitate - va fi situata in navbarul inferior si candidatii vor avea acces aici la politica de confidentialitate
                                