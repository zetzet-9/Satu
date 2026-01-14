#!/usr/bin/env python3
"""Afifah's Silly CLI — a small, funny program in Indonesian.

Usage:
  python afifah.py           # prints one quick joke and exits
  python afifah.py --interactive  # opens a small interactive menu
"""
import random
import sys
import time


JOKES = [
	"Kenapa programmer selalu bawa pulpen? Karena mereka suka mencatat bug... di kertas!",
	"Saya bilang ke komputer: 'Kamu panas!' Komputer jawab: 'Saya sedang menjalankan program panas (hotfix).',",
	"Apa kata satu bit ke bit lain? 'Kamu 1, aku 0 — mari jadi pasangan sempurna: 10!'",
	"Kenapa matematika sedih? Karena ia punya terlalu banyak masalah. Tapi jangan khawatir, saya bawa solusi: pelukan 😄",
	"Jika kucing bisa nge-commit, commit message-nya pasti 'meow: refactor paw placement'.",
]


def quick_joke():
	joke = random.choice(JOKES)
	print('\n✨ JOKE CEPAT ✨')
	print(joke)


def knock_knock():
	pairs = [
		("Knock knock","Siapa di sana?","Lettuce","Lettuce who?","Lettuce in, it's cold out here!"),
		("Knock knock","Siapa di sana?","Cow says","Cow says who?","No, silly — cow says 'moooo'!"),
	]
	a = random.choice(pairs)
	print('\n' + a[0])
	time.sleep(0.5)
	print(a[1])
	time.sleep(0.6)
	print(a[2])
	time.sleep(0.5)
	print(a[3])
	time.sleep(0.5)
	print(a[4])


def silly_poem():
	lines = [
		"Di pagi hari kopi bernyanyi,",
		"keyboard menari-nari di atas meja,",
		"seekor panda menulis puisi tentang Wi-Fi,",
		"dan semua bug berubah jadi kue rasa stroberi."
	]
	print('\n--- Puisi Konyol ---')
	for l in lines:
		print(l)
		time.sleep(0.4)


def interactive():
	while True:
		print('\nPilih aksi (ketik angka):')
		print('1) Cerita lucu singkat')
		print('2) Knock-knock (acak)')
		print('3) Puisi konyol')
		print('4) Keluar')
		choice = input('> ').strip()
		if choice == '1':
			quick_joke()
		elif choice == '2':
			knock_knock()
		elif choice == '3':
			silly_poem()
		elif choice == '4':
			print('Dadah! Semoga hari Anda penuh tawa.')
			break
		else:
			print('Pilihan tidak dikenal — coba lagi!')


def main():
	if '--interactive' in sys.argv or '-i' in sys.argv:
		interactive()
	else:
		quick_joke()


if __name__ == '__main__':
	main()

