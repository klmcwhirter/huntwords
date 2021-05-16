import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AppMaterialModule } from './app-material.module';
import { AppRoutingModule } from './app-routing.module';
import { GameStateComponent } from './game-state/game-state.component';
import { PuzzleBoardComponent } from './puzzleboard/puzzleboard.component';
import { PuzzleSelectComponent } from './puzzle-select/puzzle-select.component';

@NgModule({
  declarations: [
    AppComponent,
    GameStateComponent,
    PuzzleBoardComponent,
    PuzzleSelectComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AppMaterialModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
