import { NgModule } from '@angular/core';

import { MatCardModule } from '@angular/material/card';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatIconModule, MatIconRegistry } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';

@NgModule({
    imports: [
        MatCardModule,
        MatGridListModule,
        MatIconModule,
        MatInputModule,
        MatListModule,
    ],
    exports: [
        MatCardModule,
        MatGridListModule,
        MatIconModule,
        MatInputModule,
        MatListModule
    ],
    declarations: [],
    providers: [MatIconRegistry],
})
export class AppMaterialModule { }
