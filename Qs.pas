program gg;
const N =10;
var i  :integer;
a: array [1..N] of integer; 

function Qs(Nstart, Nend :integer):integer;
var mid,h,s,e,c: integer;                           
begin 
If (Nstart +1) >=Nend then exit;
 h:=Nstart+random(Nend-Nstart);
 mid:=A[h];
 s:=Nstart;
 e:=Nend;
 while S<e do
  begin
  while (a[s]<mid) and (s<>h) do s:=s+1;
  while (a[e]>mid) and (e<>h) do e:=e-1;
   if ((a[s]>=mid) and (a[e]<=mid)) then
    begin
    if (s=h) and (e<>h) then
     begin
    c:=a[s];
    a[s]:=a[e];
    a[e]:=A[s+1];
    a[s+1]:=c;
    s:=s+1;
    H:=H+1;
    end;
   if (e=h) and (S<>h) then
    Begin
    c:=a[e];
    a[e]:=a[s];
    a[s]:=a[e-1];
    a[e-1]:=c;
    e:=e-1;
    H:=H-1;
   
   end;
   If (E<>H) and (s<>h) then
   begin
   c:=a[e];
   a[e]:=a[s];
   a[s]:=c;
   end;
   
   end;
   end;
   
  
 
  Qs(Nstart, s);
  Qs(s, Nend);
  end;
  
  
  begin

  for i:=1 to n do 
 begin
 a[i]:=random (101);
 write (a[i], ' ');
 end;
 writeln;
Qs(1,n);
writeln;
 
 for i:=1 to n do 
  write (a[i], ' ');
 end.
  