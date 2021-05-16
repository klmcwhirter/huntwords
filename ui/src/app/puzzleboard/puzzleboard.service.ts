import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { tap } from 'rxjs/operators';
import { Puzzle } from '../puzzle/puzzle.model';
import { PuzzleBoard } from './puzzleboard.model';

const url = '/huntwords/api/huntwordsapi';

interface PuzzleBoardResponse {
    puzzleboard: PuzzleBoard;
    processed: string;
}

@Injectable({
    providedIn: 'root'
})
export class PuzzlesService {

    subjectPuzzles = new Subject<Puzzle[]>();
    puzzles$: Observable<Puzzle[]> = this.subjectPuzzles.asObservable();

    subjectPuzzleBoard = new Subject<PuzzleBoard>();
    puzzlesBoard$: Observable<PuzzleBoard> = this.subjectPuzzleBoard.asObservable();

    constructor(private http: HttpClient) { }

    getPuzzles(): void {
        console.log('getPuzzles');
        this.http.post<Puzzle[]>(url, `{ "oper": "puzzles", "body":{} }`)
            .pipe(tap(p => {
                console.log('getPuzzles: #', p.length);
                this.subjectPuzzles.next(p.sort((a: Puzzle, b: Puzzle): number => a.name.localeCompare(b.name)));
            }))
            .subscribe();
    }

    setPuzzleName(name: string): void {
        console.log('setPuzzleName: name=', name);
        this.http.post<PuzzleBoardResponse>(url, `{ "oper": "puzzleboard-pop", "body":{ "puzzle": "${name}" } }`)
            .pipe(tap(pbr => {
                const pb = pbr.puzzleboard;
                this.subjectPuzzleBoard.next(new PuzzleBoard(pb.height, pb.width, pb.letters, pb.solutions, pb.puzzle));
            }))
            .subscribe();
    }
}
