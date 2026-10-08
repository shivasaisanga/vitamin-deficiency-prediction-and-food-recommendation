// dismiss flash messages
document.querySelectorAll('.flash').forEach(f=>{
  f.querySelector('button')?.addEventListener('click',()=>f.remove());
  setTimeout(()=>f.remove(),6000);
});
// show/hide password
document.querySelectorAll('.toggle-pw').forEach(b=>b.addEventListener('click',()=>{
  const i=document.getElementById(b.dataset.target);
  const show=i.type==='password'; i.type=show?'text':'password'; b.textContent=show?'Hide':'Show';
}));
// password strength meter
const pw=document.getElementById('password'), bar=document.querySelector('.strength i');
if(pw&&bar){pw.addEventListener('input',()=>{
  const v=pw.value; let s=0;
  if(v.length>=8)s++; if(v.length>=12)s++; if(/[A-Z]/.test(v)&&/[a-z]/.test(v))s++; if(/\d/.test(v))s++; if(/[^A-Za-z0-9]/.test(v))s++;
  bar.style.width=(v?Math.max(s,1)*20:0)+'%';
  bar.style.background=['#dc2626','#dc2626','#f59e0b','#84cc16','#16a34a','#16a34a'][s];
});}
// confirm deletes
document.querySelectorAll('form[data-confirm]').forEach(f=>f.addEventListener('submit',e=>{
  if(!confirm(f.dataset.confirm))e.preventDefault();
}));
