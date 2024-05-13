

const saat = document.getElementById('saat');
const gun = document.getElementById('gun');
const tarih = document.getElementById('tarih');

function saatTarihGunu() {
    let simdikiZaman = new Date();
    let saat = simdikiZaman.toLocaleTimeString();
    let gun = simdikiZaman.getDate();
    let ay = simdikiZaman.getMonth() + 1;
    let yil = simdikiZaman.getFullYear();
    let tarih = gun + '-' + ay + '-' + yil;
    let gunler = ["Pazar", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi"];
    let gunAdi = gunler[simdikiZaman.getDay()];
    let sonuc = {
        saat: saat,
        tarih: tarih,
        gun: gunAdi
    };

    return sonuc; 
}

function saat_ayarla (){
    let result = saatTarihGunu();
    let s_tarih = String(result.tarih).replaceAll('-', '.')
    let s_gun = String(result.gun)
    gun.innerText = s_gun;
    saat.innerText = result.saat;
    tarih.innerText = s_tarih;
}


saat_ayarla();

setInterval(saat_ayarla, 1000);

