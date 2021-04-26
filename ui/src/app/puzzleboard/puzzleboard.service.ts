import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { PuzzleBoard, WordSolution } from './puzzleboard.model';

const puzzleboard: PuzzleBoard = {
    height: 15,
    width: 15,
    letters: [
        ['N', 'E', 'K', 'T', 'H', 'O', 'M', 'A', 'S', 'R', 'E', 'T', 'E', 'P', 'B'],
        ['O', 'P', 'T', 'I', 'R', 'I', 'P', 'S', 'Y', 'L', 'O', 'H', 'T', 'M', 'M'],
        ['A', 'M', 'S', 'H', 'E', 'P', 'H', 'E', 'R', 'D', 'J', 'R', 'V', 'M', 'W'],
        ['H', 'S', 'J', 'O', 'S', 'E', 'P', 'H', 'G', 'M', 'Q', 'T', 'A', 'I', 'E'],
        ['A', 'H', 'D', 'O', 'Q', 'J', 'R', 'C', 'A', 'D', 'Y', 'D', 'S', 'C', 'T'],
        ['S', 'K', 'I', 'I', 'Y', 'O', 'O', 'H', 'A', 'W', 'A', 'E', 'A', 'I', 'L'],
        ['U', 'T', 'K', 'L', 'A', 'B', 'A', 'V', 'S', 'E', 'M', 'R', 'P', 'L', 'U'],
        ['S', 'N', 'J', 'A', 'N', 'R', 'I', 'H', 'I', 'E', 'G', 'M', 'E', 'T', 'A'],
        ['E', 'R', 'W', 'A', 'B', 'D', 'E', 'J', 'N', 'T', 'L', 'U', 'S', 'J', 'P'],
        ['J', 'A', 'G', 'A', 'C', 'E', 'L', 'N', 'Z', 'S', 'M', 'G', 'G', 'S', 'L'],
        ['T', 'T', 'T', 'Q', 'P', 'O', 'H', 'T', 'I', 'A', 'F', 'W', 'J', 'E', 'P'],
        ['H', 'S', 'R', 'Y', 'R', 'D', 'B', 'N', 'S', 'C', 'N', 'O', 'P', 'T', 'E'],
        ['B', 'B', 'E', 'T', 'H', 'L', 'E', 'H', 'A', 'M', 'H', 'A', 'D', 'T', 'J'],
        ['S', 'L', 'A', 'R', 'E', 'G', 'N', 'A', 'M', 'N', 'T', 'T', 'E', 'O', 'S'],
        ['M', 'Y', 'S', 'A', 'R', 'A', 'H', 'H', 'T', 'A', 'I', 'L', 'O', 'G', 'G']
    ],
    solutions: [
        { word: 'ABRAHAM', placed: true, origin: { 'x': 10, 'y': 2 }, direction: 'NE', points: [{ 'x': 3, 'y': 9 }, { 'x': 4, 'y': 8 }, { 'x': 5, 'y': 7 }, { 'x': 6, 'y': 6 }, { 'x': 7, 'y': 5 }, { 'x': 8, 'y': 4 }, { 'x': 9, 'y': 3 }] },
        { word: 'ADAM', placed: true, origin: { 'x': 14, 'y': 1 }, direction: 'NE', points: [{ 'x': 10, 'y': 5 }, { 'x': 11, 'y': 4 }, { 'x': 12, 'y': 3 }, { 'x': 13, 'y': 2 }] },
        { word: 'BETHLEHAM', placed: true, origin: { 'x': 10, 'y': 12 }, direction: 'E', points: [{ 'x': 1, 'y': 12 }, { 'x': 2, 'y': 12 }, { 'x': 3, 'y': 12 }, { 'x': 4, 'y': 12 }, { 'x': 5, 'y': 12 }, { 'x': 6, 'y': 12 }, { 'x': 7, 'y': 12 }, { 'x': 8, 'y': 12 }, { 'x': 9, 'y': 12 }] },
        { word: 'DAVID', placed: true, origin: { 'x': 4, 'y': 9 }, direction: 'SW', points: [{ 'x': 9, 'y': 4 }, { 'x': 8, 'y': 5 }, { 'x': 7, 'y': 6 }, { 'x': 6, 'y': 7 }, { 'x': 5, 'y': 8 }] },
        { word: 'FAITH', placed: true, origin: { 'x': 5, 'y': 10 }, direction: 'W', points: [{ 'x': 10, 'y': 10 }, { 'x': 9, 'y': 10 }, { 'x': 8, 'y': 10 }, { 'x': 7, 'y': 10 }, { 'x': 6, 'y': 10 }] },
        { word: 'GOD', placed: true, origin: { 'x': 11, 'y': 11 }, direction: 'NW', points: [{ 'x': 14, 'y': 14 }, { 'x': 13, 'y': 13 }, { 'x': 12, 'y': 12 }] },
        { word: 'GOLIATH', placed: true, origin: { 'x': 6, 'y': 14 }, direction: 'W', points: [{ 'x': 13, 'y': 14 }, { 'x': 12, 'y': 14 }, { 'x': 11, 'y': 14 }, { 'x': 10, 'y': 14 }, { 'x': 9, 'y': 14 }, { 'x': 8, 'y': 14 }, { 'x': 7, 'y': 14 }] },
        { word: 'GRACE', placed: true, origin: { 'x': 15, 'y': 2 }, direction: 'NE', points: [{ 'x': 10, 'y': 7 }, { 'x': 11, 'y': 6 }, { 'x': 12, 'y': 5 }, { 'x': 13, 'y': 4 }, { 'x': 14, 'y': 3 }] },
        { word: 'HOLYSPIRIT', placed: true, origin: { 'x': 1, 'y': 1 }, direction: 'W', points: [{ 'x': 11, 'y': 1 }, { 'x': 10, 'y': 1 }, { 'x': 9, 'y': 1 }, { 'x': 8, 'y': 1 }, { 'x': 7, 'y': 1 }, { 'x': 6, 'y': 1 }, { 'x': 5, 'y': 1 }, { 'x': 4, 'y': 1 }, { 'x': 3, 'y': 1 }, { 'x': 2, 'y': 1 }] },
        { word: 'JACOB', placed: true, origin: { 'x': 7, 'y': 12 }, direction: 'SE', points: [{ 'x': 2, 'y': 7 }, { 'x': 3, 'y': 8 }, { 'x': 4, 'y': 9 }, { 'x': 5, 'y': 10 }, { 'x': 6, 'y': 11 }] },
        { word: 'JESUS', placed: true, origin: { 'x': 0, 'y': 4 }, direction: 'N', points: [{ 'x': 0, 'y': 9 }, { 'x': 0, 'y': 8 }, { 'x': 0, 'y': 7 }, { 'x': 0, 'y': 6 }, { 'x': 0, 'y': 5 }] },
        { word: 'JOB', placed: true, origin: { 'x': 5, 'y': 7 }, direction: 'S', points: [{ 'x': 5, 'y': 4 }, { 'x': 5, 'y': 5 }, { 'x': 5, 'y': 6 }] },
        { word: 'JOHN', placed: true, origin: { 'x': 8, 'y': 14 }, direction: 'SW', points: [{ 'x': 12, 'y': 10 }, { 'x': 11, 'y': 11 }, { 'x': 10, 'y': 12 }, { 'x': 9, 'y': 13 }] },
        { word: 'JOSEPH', placed: true, origin: { 'x': 8, 'y': 3 }, direction: 'E', points: [{ 'x': 2, 'y': 3 }, { 'x': 3, 'y': 3 }, { 'x': 4, 'y': 3 }, { 'x': 5, 'y': 3 }, { 'x': 6, 'y': 3 }, { 'x': 7, 'y': 3 }] },
        { word: 'MANGER', placed: true, origin: { 'x': 2, 'y': 13 }, direction: 'W', points: [{ 'x': 8, 'y': 13 }, { 'x': 7, 'y': 13 }, { 'x': 6, 'y': 13 }, { 'x': 5, 'y': 13 }, { 'x': 4, 'y': 13 }, { 'x': 3, 'y': 13 }] },
        { word: 'NOAH', placed: true, origin: { 'x': 0, 'y': 4 }, direction: 'S', points: [{ 'x': 0, 'y': 0 }, { 'x': 0, 'y': 1 }, { 'x': 0, 'y': 2 }, { 'x': 0, 'y': 3 }] },
        { word: 'PAUL', placed: true, origin: { 'x': 14, 'y': 4 }, direction: 'N', points: [{ 'x': 14, 'y': 8 }, { 'x': 14, 'y': 7 }, { 'x': 14, 'y': 6 }, { 'x': 14, 'y': 5 }] },
        { word: 'PETER', placed: true, origin: { 'x': 8, 'y': 0 }, direction: 'W', points: [{ 'x': 13, 'y': 0 }, { 'x': 12, 'y': 0 }, { 'x': 11, 'y': 0 }, { 'x': 10, 'y': 0 }, { 'x': 9, 'y': 0 }] },
        { word: 'SAMUEL', placed: true, origin: { 'x': 14, 'y': 5 }, direction: 'NE', points: [{ 'x': 8, 'y': 11 }, { 'x': 9, 'y': 10 }, { 'x': 10, 'y': 9 }, { 'x': 11, 'y': 8 }, { 'x': 12, 'y': 7 }, { 'x': 13, 'y': 6 }] },
        { word: 'SARAH', placed: true, origin: { 'x': 7, 'y': 14 }, direction: 'E', points: [{ 'x': 2, 'y': 14 }, { 'x': 3, 'y': 14 }, { 'x': 4, 'y': 14 }, { 'x': 5, 'y': 14 }, { 'x': 6, 'y': 14 }] },
        { word: 'SHEEP', placed: true, origin: { 'x': 3, 'y': 11 }, direction: 'SW', points: [{ 'x': 8, 'y': 6 }, { 'x': 7, 'y': 7 }, { 'x': 6, 'y': 8 }, { 'x': 5, 'y': 9 }, { 'x': 4, 'y': 10 }] },
        { word: 'SHEPHERD', placed: true, origin: { 'x': 10, 'y': 2 }, direction: 'E', points: [{ 'x': 2, 'y': 2 }, { 'x': 3, 'y': 2 }, { 'x': 4, 'y': 2 }, { 'x': 5, 'y': 2 }, { 'x': 6, 'y': 2 }, { 'x': 7, 'y': 2 }, { 'x': 8, 'y': 2 }, { 'x': 9, 'y': 2 }] },
        { word: 'STAR', placed: true, origin: { 'x': 1, 'y': 7 }, direction: 'N', points: [{ 'x': 1, 'y': 11 }, { 'x': 1, 'y': 10 }, { 'x': 1, 'y': 9 }, { 'x': 1, 'y': 8 }] },
        { word: 'THOMAS', placed: true, origin: { 'x': 9, 'y': 0 }, direction: 'E', points: [{ 'x': 3, 'y': 0 }, { 'x': 4, 'y': 0 }, { 'x': 5, 'y': 0 }, { 'x': 6, 'y': 0 }, { 'x': 7, 'y': 0 }, { 'x': 8, 'y': 0 }] },
        { word: 'WISEMEN', placed: true, origin: { 'x': 7, 'y': 9 }, direction: 'SW', points: [{ 'x': 14, 'y': 2 }, { 'x': 13, 'y': 3 }, { 'x': 12, 'y': 4 }, { 'x': 11, 'y': 5 }, { 'x': 10, 'y': 6 }, { 'x': 9, 'y': 7 }, { 'x': 8, 'y': 8 }] }
    ],
    puzzle: { name: 'Bible', description: 'Words from the bible', words: ['ABRAHAM', 'ADAM', 'BETHLEHAM', 'DANIEL', 'DAVID', 'ELIJAH', 'ELISHA', 'EVE', 'FAITH', 'GOD', 'GOLIATH', 'GRACE', 'HEALING', 'HOLYSPIRIT', 'ISRAEL', 'JACOB', 'JESUS', 'JOB', 'JOHN', 'JOSEPH', 'MANGER', 'MARY', 'NOAH', 'PAUL', 'PETER', 'SAMUEL', 'SARAH', 'SHEEP', 'SHEPHERD', 'STAR', 'THOMAS', 'WISEMEN'] },
    displayedWordSolutions: [] as WordSolution[],
    wordListCols: 0,
    wordsPlacedCount: 0,
    wordsNotSelectedCount: 0,
    wordsSelectedCount: 0
};

@Injectable({
    providedIn: 'root'
})
export class PuzzleBoardService {
    getPuzzleBoard(name: string): Observable<PuzzleBoard> {
        return of(new PuzzleBoard(puzzleboard.height, puzzleboard.width, puzzleboard.letters, puzzleboard.solutions, puzzleboard.puzzle));
    }
}
