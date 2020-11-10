import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { environment } from 'src/environments/environment';
import { CountResponse } from './type';

@Injectable({
  providedIn: 'root'
})
export class CounterService {
  private _url = `${environment.apiUrl}/counter/`

  constructor(
    private http: HttpClient
  ) { }

  getCount() {
    return this.http.get<CountResponse>(`${this._url}`);
  }

  decreaseCount() {
    return this.http.post<CountResponse>(`${this._url}`, {});
  }
}
