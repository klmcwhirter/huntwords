import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AppMaterialModule } from './app-material.module';
import { AppRoutingModule } from './app-routing.module';
import { PuzzleBoardComponent } from './puzzleboard/puzzleboard.component';

@NgModule({
  declarations: [
    AppComponent,
    PuzzleBoardComponent
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
