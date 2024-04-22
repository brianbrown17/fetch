import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AgmCoreModule } from '@agm/core';

const routes: Routes = [];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyAK7y39CILuS-5jYUzhQmmwz24z8UaFFpQ'
    })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
