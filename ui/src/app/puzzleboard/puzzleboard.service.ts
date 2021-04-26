import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { PuzzleBoard } from './puzzleboard.model';

const puzzleboard: PuzzleBoard = {
    height: 15,
    width: 15,
    letters: [
        ['N', 'L', 'Z', 'E', 'R', 'L', 'E', 'U', 'M', 'A', 'S', 'J', 'W', 'O', 'K'],
        ['D', 'E', 'I', 'V', 'F', 'H', 'T', 'A', 'I', 'L', 'O', 'G', 'D', 'E', 'M'],
        ['V', 'A', 'D', 'E', 'L', 'X', 'X', 'V', 'M', 'A', 'H', 'A', 'R', 'B', 'A'],
        ['H', 'R', 'I', 'F', 'W', 'D', 'Y', 'H', 'A', 'O', 'N', 'A', 'D', 'A', 'M'],
        ['P', 'S', 'S', 'F', 'X', 'G', 'W', 'H', 'T', 'A', 'I', 'L', 'O', 'G', 'K'],
        ['E', 'I', 'S', 'E', 'R', 'A', 'T', 'S', 'M', 'A', 'H', 'A', 'R', 'B', 'A'],
        ['S', 'G', 'Z', 'A', 'H', 'X', 'J', 'T', 'R', 'O', 'U', 'B', 'O', 'L', 'S'],
        ['O', 'M', 'C', 'S', 'L', 'I', 'S', 'U', 'S', 'E', 'J', 'M', 'W', 'W', 'A'],
        ['J', 'E', 'I', 'W', 'I', 'S', 'E', 'M', 'E', 'N', 'G', 'V', 'A', 'W', 'M'],
        ['I', 'L', 'P', 'B', 'B', 'B', 'R', 'N', 'Y', 'X', 'S', 'N', 'G', 'U', 'O'],
        ['E', 'X', 'X', 'Y', 'R', 'A', 'M', 'G', 'K', 'R', 'L', 'U', 'A', 'G', 'H'],
        ['P', 'I', 'T', 'M', 'A', 'I', 'W', 'L', 'L', 'Y', 'A', 'W', 'S', 'M', 'T'],
        ['U', 'B', 'Z', 'T', 'K', 'E', 'N', 'H', 'O', 'J', 'U', 'M', 'I', 'E', 'B'],
        ['B', 'E', 'T', 'H', 'L', 'E', 'H', 'A', 'M', 'G', 'C', 'J', 'K', 'O', 'J'],
        ['L', 'E', 'I', 'N', 'A', 'D', 'W', 'H', 'T', 'I', 'A', 'F', 'J', 'X', 'N']
    ],
    solutions: [
        {
            word: 'BETHLEHAM', placed: true, origin: { x: 9, y: 13 }, direction: 'E', points: [
                { x: 0, y: 13 },
                { x: 1, y: 13 },
                { x: 2, y: 13 },
                { x: 3, y: 13 },
                { x: 4, y: 13 },
                { x: 5, y: 13 },
                { x: 6, y: 13 },
                { x: 7, y: 13 },
                { x: 8, y: 13 }
            ]
        },
        {
            word: 'WISEMEN', placed: true, origin: { x: 10, y: 8 }, direction: 'E', points: [
                { x: 3, y: 8 },
                { x: 4, y: 8 },
                { x: 5, y: 8 },
                { x: 6, y: 8 },
                { x: 7, y: 8 },
                { x: 8, y: 8 },
                { x: 9, y: 8 }
            ]
        },
        {
            word: 'STAR', placed: true, origin: { x: 3, y: 5 }, direction: 'W', points: [
                { x: 7, y: 5 },
                { x: 6, y: 5 },
                { x: 5, y: 5 },
                { x: 4, y: 5 }
            ]
        },
        {
            word: 'SAMUEL', placed: true, origin: { x: 4, y: 0 }, direction: 'W', points: [
                { x: 10, y: 0 },
                { x: 9, y: 0 },
                { x: 8, y: 0 },
                { x: 7, y: 0 },
                { x: 6, y: 0 },
                { x: 5, y: 0 }
            ]
        },
        {
            word: 'MANGER', placed: true, origin: { x: 7, y: 5 }, direction: 'NW', points: [
                { x: 13, y: 11 },
                { x: 12, y: 10 },
                { x: 11, y: 9 },
                { x: 10, y: 8 },
                { x: 9, y: 7 },
                { x: 8, y: 6 }
            ]
        },
        {
            word: 'JOB', placed: true, origin: { x: 15, y: 11 }, direction: 'NE', points: [
                { x: 12, y: 14 },
                { x: 13, y: 13 },
                { x: 14, y: 12 }
            ]
        },
        {
            word: 'JOSEPH', placed: true, origin: { x: 0, y: 2 }, direction: 'N', points: [
                { x: 0, y: 8 },
                { x: 0, y: 7 },
                { x: 0, y: 6 },
                { x: 0, y: 5 },
                { x: 0, y: 4 },
                { x: 0, y: 3 }
            ]
        },
        {
            word: 'ABRAHAM', placed: true, origin: { x: 7, y: 5 }, direction: 'W', points: [
                { x: 14, y: 5 },
                { x: 13, y: 5 },
                { x: 12, y: 5 },
                { x: 11, y: 5 },
                { x: 10, y: 5 },
                { x: 9, y: 5 },
                { x: 8, y: 5 }
            ]
        },
        {
            word: 'ADAM', placed: true, origin: { x: 15, y: 3 }, direction: 'E', points: [
                { x: 11, y: 3 },
                { x: 12, y: 3 },
                { x: 13, y: 3 },
                { x: 14, y: 3 }
            ]
        },
        {
            word: 'JOHN', placed: true, origin: { x: 5, y: 12 }, direction: 'W', points: [
                { x: 9, y: 12 },
                { x: 8, y: 12 },
                { x: 7, y: 12 },
                { x: 6, y: 12 }
            ]
        },
        {
            word: 'GRACE', placed: true, origin: { x: 0, y: 9 }, direction: 'SW', points: [
                { x: 5, y: 4 },
                { x: 4, y: 5 },
                { x: 3, y: 6 },
                { x: 2, y: 7 },
                { x: 1, y: 8 }
            ]
        },
        {
            word: 'EVE', placed: true, origin: { x: 3, y: -1 }, direction: 'N', points: [
                { x: 3, y: 2 },
                { x: 3, y: 1 },
                { x: 3, y: 0 }
            ]
        },
        {
            word: 'ELISHA', placed: true, origin: { x: 6, y: 4 }, direction: 'NE', points: [
                { x: 0, y: 10 },
                { x: 1, y: 9 },
                { x: 2, y: 8 },
                { x: 3, y: 7 },
                { x: 4, y: 6 },
                { x: 5, y: 5 }
            ]
        },
        {
            word: 'GOLIATH', placed: true, origin: { x: 6, y: 4 }, direction: 'W', points: [
                { x: 13, y: 4 },
                { x: 12, y: 4 },
                { x: 11, y: 4 },
                { x: 10, y: 4 },
                { x: 9, y: 4 },
                { x: 8, y: 4 },
                { x: 7, y: 4 }
            ]
        },
        {
            word: 'JESUS', placed: true, origin: { x: 9, y: 8 }, direction: 'NW', points: [
                { x: 14, y: 13 },
                { x: 13, y: 12 },
                { x: 12, y: 11 },
                { x: 11, y: 10 },
                { x: 10, y: 9 }
            ]
        },
        {
            word: 'THOMAS', placed: true, origin: { x: 14, y: 5 }, direction: 'N', points: [
                { x: 14, y: 11 },
                { x: 14, y: 10 },
                { x: 14, y: 9 },
                { x: 14, y: 8 },
                { x: 14, y: 7 },
                { x: 14, y: 6 }
            ]
        },
        {
            word: 'ISRAEL', placed: true, origin: { x: 1, y: -1 }, direction: 'N', points: [
                { x: 1, y: 5 },
                { x: 1, y: 4 },
                { x: 1, y: 3 },
                { x: 1, y: 2 },
                { x: 1, y: 1 },
                { x: 1, y: 0 }
            ]
        },
        {
            word: 'MARY', placed: true, origin: { x: 7, y: 8 }, direction: 'NW', points: [
                { x: 11, y: 12 },
                { x: 10, y: 11 },
                { x: 9, y: 10 },
                { x: 8, y: 9 }
            ]
        },
        {
            word: 'DANIEL', placed: true, origin: { x: -1, y: 14 }, direction: 'W', points: [
                { x: 5, y: 14 },
                { x: 4, y: 14 },
                { x: 3, y: 14 },
                { x: 2, y: 14 },
                { x: 1, y: 14 },
                { x: 0, y: 14 }
            ]
        },
        {
            word: 'JESUS', placed: true, origin: { x: 5, y: 7 }, direction: 'W', points: [
                { x: 10, y: 7 },
                { x: 9, y: 7 },
                { x: 8, y: 7 },
                { x: 7, y: 7 },
                { x: 6, y: 7 }
            ]
        },
        {
            word: 'GOLIATH', placed: true, origin: { x: 4, y: 1 }, direction: 'W', points: [
                { x: 11, y: 1 },
                { x: 10, y: 1 },
                { x: 9, y: 1 },
                { x: 8, y: 1 },
                { x: 7, y: 1 },
                { x: 6, y: 1 },
                { x: 5, y: 1 }
            ]
        },
        {
            word: 'FAITH', placed: true, origin: { x: 6, y: 14 }, direction: 'W', points: [
                { x: 11, y: 14 },
                { x: 10, y: 14 },
                { x: 9, y: 14 },
                { x: 8, y: 14 },
                { x: 7, y: 14 }
            ]
        },
        {
            word: 'NOAH', placed: true, origin: { x: 6, y: 3 }, direction: 'W', points: [
                { x: 10, y: 3 },
                { x: 9, y: 3 },
                { x: 8, y: 3 },
                { x: 7, y: 3 }
            ]
        },
        {
            word: 'ABRAHAM', placed: true, origin: { x: 7, y: 2 }, direction: 'W', points: [
                { x: 14, y: 2 },
                { x: 13, y: 2 },
                { x: 12, y: 2 },
                { x: 11, y: 2 },
                { x: 10, y: 2 },
                { x: 9, y: 2 },
                { x: 8, y: 2 }
            ]
        },
        {
            word: 'MARY', placed: true, origin: { x: 2, y: 10 }, direction: 'W', points: [
                { x: 6, y: 10 },
                { x: 5, y: 10 },
                { x: 4, y: 10 },
                { x: 3, y: 10 }
            ]
        }
    ],
    puzzle: {
        name: 'Bible',
        description: 'Words from the bible',
        words: [
            'ABRAHAM', 'ADAM', 'BETHLEHAM', 'DANIEL', 'DAVID', 'ELIJAH', 'ELISHA', 'EVE', 'FAITH', 'GOD', 'GOLIATH', 'GRACE', 'HEALING', 'HOLYSPIRIT', 'ISRAEL', 'JACOB', 'JESUS', 'JOB', 'JOHN', 'JOSEPH', 'MANGER', 'MARY', 'NOAH', 'PAUL', 'PETER', 'SAMUEL', 'SARAH', 'SHEEP', 'SHEPHERD', 'STAR', 'THOMAS', 'WISEMEN'
        ]
    }
};


@Injectable({
  providedIn: 'root'
})
export class PuzzleBoardService {
    getPuzzleBoard(name: string): Observable<PuzzleBoard> {
        return of(new PuzzleBoard(puzzleboard.height, puzzleboard.width, puzzleboard.letters, puzzleboard.solutions, puzzleboard.puzzle));
    }
}
